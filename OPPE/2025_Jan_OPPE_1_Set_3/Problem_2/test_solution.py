import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.upper_nth_index_char("hello", 0) == "Hello"

def test_2():
    assert solution.upper_nth_index_char("hello", 4) == "hellO"

def test_3():
    assert solution.upper_nth_index_char("hello", 5) == "hello"

def test_4():
    assert solution.upper_nth_index_char("world", 2) == "woRld"

def test_private():
    assert solution.upper_nth_index_char("", 0) == ""
    assert solution.upper_nth_index_char("a", 0) == "A"
