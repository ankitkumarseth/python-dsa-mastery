import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.is_odd_length_palindrome("a") is True

def test_2():
    assert solution.is_odd_length_palindrome("racecar") is True

def test_3():
    assert solution.is_odd_length_palindrome("noon") is False

def test_4():
    assert solution.is_odd_length_palindrome("hello") is False
