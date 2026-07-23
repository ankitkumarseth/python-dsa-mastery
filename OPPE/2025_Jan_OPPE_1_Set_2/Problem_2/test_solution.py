import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.is_rotation('abcde', 'cdeab') is True

def test_2():
    assert solution.is_rotation('abcde', 'edcba') is False

def test_3():
    assert solution.is_rotation('abcde', ' ') is False

def test_4():
    assert solution.is_rotation("abcde", "eab") is False

def test_5():
    assert solution.is_rotation("abcde", "abcdea") is False
