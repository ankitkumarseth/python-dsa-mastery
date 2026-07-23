import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.is_even_or_divisible_by_5(25) is True

def test_2():
    assert solution.is_even_or_divisible_by_5(1013) is False

def test_3():
    assert solution.is_even_or_divisible_by_5(1000) is True

def test_4():
    assert solution.is_even_or_divisible_by_5(48) is True
    
# Extra private tests
def test_private():
    assert solution.is_even_or_divisible_by_5(0) is True
    assert solution.is_even_or_divisible_by_5(-5) is True
    assert solution.is_even_or_divisible_by_5(-4) is True
