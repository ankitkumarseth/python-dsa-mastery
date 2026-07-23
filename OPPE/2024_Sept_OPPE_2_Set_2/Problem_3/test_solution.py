import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.number_with_more_unique_digits(2345, 1111) == 2345

def test_2():
    assert solution.number_with_more_unique_digits(222333, 22334) == 22334

def test_3():
    assert solution.number_with_more_unique_digits(123456, 11223344) == 123456

def test_4():
    assert solution.number_with_more_unique_digits(1234, 11223344) == (1234, 11223344)
