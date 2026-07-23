import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.is_even_two_digit_number(24) is True

def test_2():
    assert solution.is_even_two_digit_number(101) is False

def test_3():
    assert solution.is_even_two_digit_number(-18) is True
