import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.is_even_and_second_last_digit_is_two(124) is True

def test_2():
    assert solution.is_even_and_second_last_digit_is_two(430) is False

def test_3():
    assert solution.is_even_and_second_last_digit_is_two(185) is False

def test_4():
    assert solution.is_even_and_second_last_digit_is_two(13) is False

def test_private():
    assert solution.is_even_and_second_last_digit_is_two(-22) is True
    assert solution.is_even_and_second_last_digit_is_two(2) is False
