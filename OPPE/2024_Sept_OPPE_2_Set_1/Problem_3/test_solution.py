import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.is_present_in_opposite_halves(3, [1, 2, 3, 4], [3, 4, 5, 6]) is True

def test_2():
    assert solution.is_present_in_opposite_halves(7, [1, 2, 3, 4], [5, 6, 3, 8]) is False

def test_3():
    assert solution.is_present_in_opposite_halves(6, [5, 6, 7, 8], [1, 2, 6, 4]) is True

def test_4():
    assert solution.is_present_in_opposite_halves(1, [1, 2, 4, 3, 3, 4], [5, 1, 3, 4, 3, 8]) is False
