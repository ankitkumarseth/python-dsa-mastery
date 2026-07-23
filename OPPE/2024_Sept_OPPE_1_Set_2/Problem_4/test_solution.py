import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.count_positive_ignore_none([1, -2, 3, 0, None, 4]) == 3

def test_2():
    assert solution.count_positive_ignore_none([0, -1, None, -3]) == 0

def test_3():
    assert solution.count_positive_ignore_none([None, 5, 7, 8]) == 3
