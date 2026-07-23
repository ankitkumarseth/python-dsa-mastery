import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.sum_of_squares_of_even([1, 2, 3, 4, 5, 6]) == 56

def test_2():
    assert solution.sum_of_squares_of_even([10, 15, 20, 25, 30]) == 1400

def test_3():
    assert solution.sum_of_squares_of_even([1, 3, 5, 7]) == 0
