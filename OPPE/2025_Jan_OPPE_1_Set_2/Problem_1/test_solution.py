import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.is_both_divisible_by(10, 15, 5) is True

def test_2():
    assert solution.is_both_divisible_by(12, 19, 6) is False

def test_3():
    assert solution.is_both_divisible_by(-12, -18, 6) is True

def test_4():
    assert solution.is_both_divisible_by(15, 16, 7) is False
