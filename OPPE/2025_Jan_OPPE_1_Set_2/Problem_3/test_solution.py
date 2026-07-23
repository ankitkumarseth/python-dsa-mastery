import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.find_missing_number([1,2,4,5,6], 6) == 3
    assert solution.find_missing_number([1,3,3,4,5,5,6], 6) == 2

def test_2():
    assert solution.find_missing_number([2, 3, 4, 5], 5) == 1
    assert solution.find_missing_number([5, 4, 3, 1], 5) == 2

def test_3():
    assert solution.find_missing_number([1, 2, 3, 4, 5, 6, 8, 9, 10], 10) == 7
