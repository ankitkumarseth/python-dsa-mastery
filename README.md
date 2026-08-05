# IITM Python Practice

A structured repository for practicing and mastering Python concepts for IITM coursework. 

## Structure

The repository is divided into two main domains:
1. **GrPA (Graded Programming Assignments)**: Dedicated folders for topic-by-topic mastery (e.g., Loops, Collections, Dictionaries).
2. **OPPE (Online Proctored Programming Exams)**: Mixed-topic mock exams to test your comprehensive knowledge. The repository includes 14 fully scaffolded OPPE sets across 2024 and 2025 (e.g., 2024 May, 2024 Sept, 2025 Jan) for extensive practice.

## Repository Branches

To maximize practice value, this repository utilizes two primary branches:
1. **`main`**: The practice branch. Contains all folder structures, problem descriptions (`README.md`), unit tests, and heavily documented `solution.py` files with their implementations wiped (only `pass` remains). 
2. **`solution`**: The answer key branch. Contains the fully working, tested implementations for every problem in the repository. If you get stuck while practicing on `main`, you can switch to `solution` to see the reference answers!

## How to Practice

Every question comes with:
* `README.md`: The problem statement and instructions.
* `solution.py`: Your workspace to write the code.
* `test_solution.py`: A robust test suite.

To check your answer for a specific topic, navigate to its folder in your terminal (or use your IDE's test runner) and run `pytest`. 

```bash
cd GrPA/10_dictionary_basics
pytest
```

> Note: Certain problems enforce strict rules (e.g., no `for` loops or `if` statements). These are automatically checked by the testing suite when applicable.
