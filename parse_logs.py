"""
Robust log parsing utility for lines in the form:
    [LEVEL] YYYY-MM-DD HH:MM:SS - message

Outputs dicts of the form:
    {"level": "LEVEL", "timestamp": "YYYY-MM-DD", "message": "..."}

This avoids IndexError seen when splitting on spaces in the bracketed token.
"""
from __future__ import annotations
import re
from typing import Iterable, List, Dict

# Regex capturing: level, date-only, and message
LOG_PATTERN = re.compile(
    r"^\[(?P<level>[A-Z]+)]\s+(?P<date>\d{4}-\d{2}-\d{2})\s+\d{2}:\d{2}:\d{2}\s*-\s*(?P<message>.*)$"
)


def parse_logs(logs: Iterable[str]) -> List[Dict[str, str]]:
    """Parse logs into structured dicts.

    - Extracts level from [LEVEL]
    - Extracts date (not time) from timestamp
    - Extracts message after the first " - "
    - Gracefully handles slightly malformed lines; falls back without raising
    """
    parsed: List[Dict[str, str]] = []
    for raw in logs:
        log = (raw or "").strip()
        if not log:
            continue
        m = LOG_PATTERN.match(log)
        if m:
            parsed.append({
                "level": m.group("level"),
                "timestamp": m.group("date"),
                "message": m.group("message"),
            })
            continue
        # Fallback: tolerant parsing without assumptions that cause IndexError
        try:
            rb = log.index("]")  # end of [LEVEL]
            level = log[1:rb]
            after = log[rb + 1 :].lstrip()  # e.g., '2025-03-07 12:00:01 - ...'
            ts_part, _sep, message = after.partition(" - ")
            date = ts_part.split()[0] if ts_part else ""
            parsed.append({"level": level, "timestamp": date, "message": message})
        except Exception:
            # If even fallback fails, capture the raw line for visibility
            parsed.append({"level": "", "timestamp": "", "message": log})
    return parsed


if __name__ == "__main__":
    logs = [
        "[INFO] 2025-03-07 12:00:01 - User login: john_doe",
        "[ERROR] 2025-03-07 12:02:15 - Database timeout",
        "[WARNING] 2025-03-07 12:05:42 - Low disk space",
    ]
    expected = [
        {"level": "INFO", "timestamp": "2025-03-07", "message": "User login: john_doe"},
        {"level": "ERROR", "timestamp": "2025-03-07", "message": "Database timeout"},
        {"level": "WARNING", "timestamp": "2025-03-07", "message": "Low disk space"},
    ]

    result = parse_logs(logs)
    print(result)
    assert result == expected, "Parsed logs do not match expected structure"