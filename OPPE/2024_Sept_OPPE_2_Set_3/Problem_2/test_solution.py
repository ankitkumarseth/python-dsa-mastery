import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.is_divisible_by_last_two_digits(1464) is True

def test_2():
    assert solution.is_divisible_by_last_two_digits(4263) is False
    assert solution.is_divisible_by_last_two_digits(275) is False
    assert solution.is_divisible_by_last_two_digits(8038) is False

def test_3():
    assert solution.is_divisible_by_last_two_digits(410) is False
    assert solution.is_divisible_by_last_two_digits(605) is False
