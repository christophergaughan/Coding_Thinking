# 🐍 Intermediate Python Concepts — With Dockerized Environment

> ⚠️ **This repo is under active development**  
> It aims to reinforce key intermediate concepts in Python through repeated examples, especially around efficient data structures and function design.

---

## 📚 Project Overview

This repository focuses on **intermediate-level Python coding** concepts and best practices. It features code patterns commonly used in:

- 🧠 **Algorithm design**
- 📦 **Data structure manipulation**
- ⚡ **Fast lookups** using `sets` and `dictionaries`
- 🔁 Repeated examples that reinforce:
  - Custom functions
  - Conditional logic
  - Iteration & list comprehension
  - Membership checks
  - Dictionary comprehensions

> The goal is to build a strong intuition around Python’s efficient built-in tools and reusable coding patterns.

---

## 🐳 Docker Environment

This project is fully containerized using Docker, with a clean Python + Conda setup inside the image for consistent reproducibility across machines.

### 🛠 Base Environment Includes:
- `Python 3.10.14`
- `Miniconda`
- `JupyterLab`
- Support for future ML/DL/data workflows if needed

### 🔧 `Dockerfile` Summary:
- Starts from `continuumio/miniconda3`
- Installs a Conda environment named `data_ml_env`
- Automatically launches `JupyterLab` on port `8888`
- Disables password/token auth for faster local development
- Includes pip-installed packages like:
  - `numpy`, `pandas`, `matplotlib`, `scikit-learn`, `seaborn`
  - `jupyterlab`, `notebook`

---

## 🚀 Getting Started

### 1. **Clone the repo**
```
git clone https://github.com/christophergaughan/Coding_Thinking
cd your-repo-name
```
## Build the Docker image
`docker build -t data_ml_env .`

## Run the container
`docker run -p 8888:8888 -v $(pwd):/app -it data_ml_env`
JupyterLab will automatically launch, and you can open it in your browser:
`http://127.0.0.1:8888/lab`
No token or password is required.

## 📁 Directory Structure
.
├── Dockerfile
├── environment.yml
├── notebooks/
│   ├── sets_and_dicts.ipynb
│   ├── function_patterns.ipynb
│   └── ...
├── scripts/
│   └── example_snippets.py
├── README.md

## 🧠 Concepts Covered (In Progress)
* `set()` vs `list` for membership checks
* `dict.get()` for fast default handling
* Dictionary comprehension
* Looping patterns and idioms
* `enumerate()` vs `range(len(...))`
* Custom function design patterns
* Error handling & try/except use cases
* And more to come...

## 📌 Future Improvements
 * Add example walkthroughs for collections.defaultdict and Counter
 * Integrate type hints and basic testing
 * Explore dataclasses and basic OOP
 * Add ML notebooks (e.g., sklearn pipeline, model evaluation)

## 🤝 Contributing
**This is a personal learning project for now, but PRs and suggestions are welcome.**

## License
This project is licensed under the MIT License.




