# Python & DSA Mastery

A unified workspace for mastering Core Python engineering and Data Structures & Algorithms (DSA). This repository is divided into two distinct tracks to streamline interview preparation and deep conceptual learning.

## 1. Python Core (IITM Practice)

Located in the root directory (GrPA, PPA, OPPE folders), this track focuses on deep Python syntax and advanced mechanics.

*   **GrPA/PPA**: Dedicated folders for topic-by-topic mastery (e.g., Loops, Collections, Dictionaries).
*   **OPPE**: Mixed-topic mock exams to test comprehensive knowledge, including 14 fully scaffolded sets from 2024 and 2025.
*   **Master Cheatsheet**: Refer to `python_master_cheatsheet.md` for advanced syntax, functional programming, and recursion patterns.

### Branching Strategy
*   **`main`**: The practice branch. Contains all problems and tests, but implementations are wiped (`pass`).
*   **`solution`**: The answer key branch. Contains the fully working, tested implementations for every Python problem.

## 2. DSA Mastery

Located in the `dsa/` directory, this track is heavily tailored toward cracking top-tier engineering interviews, specifically targeting the LeetCode 150 patterns.

*   **Curriculum**: See `dsa/dsa_master_curriculum.md` for the prioritized checklist of patterns (Arrays, Two Pointers, Linked Lists, Trees, etc.).
*   **Implementations**: The `dsa/src/` folder contains clean, Principal-level Python implementations of core algorithms.
*   **Testing**: The `dsa/tests/` folder contains Pytest suites to validate every algorithm's edge cases.

## Getting Started

To validate your code for either track, navigate to the specific problem or pattern folder and run pytest:

```bash
# Testing a Python Core problem
cd GrPA/10_dictionary_basics
pytest

# Testing a DSA pattern
cd dsa
pytest tests/test_two_pointers.py
```
