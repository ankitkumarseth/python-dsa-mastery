import os
import sys
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.sum_squares_abs_diff_squares(1, 2) == (5, 3)

def test_2():
    assert solution.sum_squares_abs_diff_squares(-1, 5) == (26, 24)

def test_3():
    assert solution.sum_squares_abs_diff_squares(2345, 2345) == (10998050, 0)
