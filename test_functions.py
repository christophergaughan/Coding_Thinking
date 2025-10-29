"""
Unit tests for various coding problems:
1. parse_logs - Log parsing with structured output
2. canConstruct - Ransom note construction from magazine
3. numJewelsInStones - Count jewels in stones
4. get_sum - Calculate sum of linked list values
"""
import unittest
from collections import defaultdict


# Define ListNode for linked list tests
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Import or define the functions to test
from parse_logs import parse_logs


def canConstruct(ransomNote, magazine):
    """Check if ransom note can be constructed from magazine letters."""
    magazine_dict = defaultdict(int)
    ransom_dict = defaultdict(int)
    
    for char in magazine:
        magazine_dict[char] += 1
    
    for char in ransomNote:
        ransom_dict[char] += 1
    
    for k, v in ransom_dict.items():
        if magazine_dict[k] < v:
            return False
    return True


def numJewelsInStones(jewels, stones):
    """Count how many stones are jewels."""
    st_jls = set(jewels)
    counter = 0
    
    for s in stones:
        if s in st_jls:
            counter += 1
    
    return counter


def get_sum(head):
    """Calculate sum of all values in a linked list (iterative)."""
    ans = 0
    while head:
        ans += head.val
        head = head.next
    return ans


class TestParseLogs(unittest.TestCase):
    """Test cases for parse_logs function."""
    
    def test_well_formed_log_lines(self):
        """Test that parse_logs correctly extracts level, date, and message from well-formed log lines."""
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
        self.assertEqual(result, expected)
    
    def test_malformed_log_lines_graceful_fallback(self):
        """Test that parse_logs handles malformed log lines gracefully with fallback."""
        # Test various malformed inputs
        logs = [
            "[DEBUG] Malformed line without proper timestamp",
            "No brackets here at all",
            "[INFO] 2025-03-07 12:00:01 - Valid line",
            "",  # Empty line
            "   ",  # Whitespace only
        ]
        
        result = parse_logs(logs)
        
        # Should return some results (at least the valid one)
        self.assertGreater(len(result), 0)
        
        # The valid line should be parsed correctly
        valid_entry = next((r for r in result if r.get("level") == "INFO"), None)
        self.assertIsNotNone(valid_entry)
        self.assertEqual(valid_entry["timestamp"], "2025-03-07")
        self.assertEqual(valid_entry["message"], "Valid line")
        
        # Malformed lines should either have empty fields or raw message
        for entry in result:
            self.assertIn("level", entry)
            self.assertIn("timestamp", entry)
            self.assertIn("message", entry)
    
    def test_empty_logs_list(self):
        """Test that parse_logs handles an empty list."""
        result = parse_logs([])
        self.assertEqual(result, [])
    
    def test_log_with_hyphen_in_message(self):
        """Test that parse_logs correctly handles messages containing hyphens."""
        logs = ["[INFO] 2025-03-07 12:00:01 - User action: test-case-with-hyphens"]
        result = parse_logs(logs)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["message"], "User action: test-case-with-hyphens")


class TestCanConstruct(unittest.TestCase):
    """Test cases for canConstruct function (ransom note problem)."""
    
    def test_can_construct_true_exact_match(self):
        """Test that canConstruct returns True when magazine has exact letters needed."""
        self.assertTrue(canConstruct("aa", "aab"))
    
    def test_can_construct_false_insufficient_letters(self):
        """Test that canConstruct returns False when magazine lacks required letters."""
        self.assertFalse(canConstruct("aa", "ab"))
    
    def test_can_construct_false_wrong_letter(self):
        """Test that canConstruct returns False when magazine has wrong letters."""
        self.assertFalse(canConstruct("a", "b"))
    
    def test_can_construct_true_extra_letters(self):
        """Test that canConstruct returns True when magazine has extra letters."""
        self.assertTrue(canConstruct("abc", "aabbcc"))
    
    def test_can_construct_empty_ransom_note(self):
        """Test that empty ransom note always returns True."""
        self.assertTrue(canConstruct("", "abc"))
    
    def test_can_construct_empty_magazine(self):
        """Test that non-empty ransom note with empty magazine returns False."""
        self.assertFalse(canConstruct("a", ""))
    
    def test_can_construct_case_sensitive(self):
        """Test that canConstruct is case-sensitive."""
        self.assertFalse(canConstruct("a", "A"))
        self.assertFalse(canConstruct("A", "a"))


class TestNumJewelsInStones(unittest.TestCase):
    """Test cases for numJewelsInStones function."""
    
    def test_jewels_in_stones_basic(self):
        """Test basic case where some stones are jewels."""
        result = numJewelsInStones("aA", "aAAbbbb")
        self.assertEqual(result, 3)
    
    def test_jewels_in_stones_no_match(self):
        """Test case where no stones are jewels."""
        result = numJewelsInStones("z", "ZZ")
        self.assertEqual(result, 0)
    
    def test_jewels_in_stones_all_match(self):
        """Test case where all stones are jewels."""
        result = numJewelsInStones("abc", "aabbcc")
        self.assertEqual(result, 6)
    
    def test_jewels_in_stones_case_sensitive(self):
        """Test that function correctly handles case sensitivity."""
        result = numJewelsInStones("aA", "aabbAABB")
        self.assertEqual(result, 4)  # 2 'a' + 2 'A'
    
    def test_jewels_in_stones_empty_jewels(self):
        """Test with empty jewels string."""
        result = numJewelsInStones("", "aabbcc")
        self.assertEqual(result, 0)
    
    def test_jewels_in_stones_empty_stones(self):
        """Test with empty stones string."""
        result = numJewelsInStones("abc", "")
        self.assertEqual(result, 0)


class TestGetSum(unittest.TestCase):
    """Test cases for get_sum function (linked list sum)."""
    
    def test_get_sum_single_node(self):
        """Test sum of linked list with single node."""
        head = ListNode(5)
        self.assertEqual(get_sum(head), 5)
    
    def test_get_sum_multiple_nodes(self):
        """Test sum of linked list with multiple nodes."""
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        self.assertEqual(get_sum(head), 6)
    
    def test_get_sum_empty_list(self):
        """Test sum of empty linked list."""
        self.assertEqual(get_sum(None), 0)
    
    def test_get_sum_negative_values(self):
        """Test sum with negative values."""
        head = ListNode(-5)
        head.next = ListNode(3)
        head.next.next = ListNode(-2)
        self.assertEqual(get_sum(head), -4)
    
    def test_get_sum_zero_values(self):
        """Test sum with zero values."""
        head = ListNode(0)
        head.next = ListNode(0)
        head.next.next = ListNode(0)
        self.assertEqual(get_sum(head), 0)
    
    def test_get_sum_large_list(self):
        """Test sum of larger linked list."""
        head = ListNode(1)
        current = head
        for i in range(2, 11):  # Create list 1->2->3->...->10
            current.next = ListNode(i)
            current = current.next
        self.assertEqual(get_sum(head), 55)  # Sum of 1 to 10


if __name__ == "__main__":
    unittest.main()
