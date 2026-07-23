import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.within_and_has_double_quotes('"abcd"efgh"') is True

def test_2():
    assert solution.within_and_has_double_quotes('"abcdefgh"') is False

def test_3():
    assert solution.within_and_has_double_quotes('abcd"efgh"') is False

def test_4():
    assert solution.within_and_has_double_quotes("'abcd'efgh'") is False
