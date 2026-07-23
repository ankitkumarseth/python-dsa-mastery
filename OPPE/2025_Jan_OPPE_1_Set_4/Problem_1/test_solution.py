import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.is_obtuse(30, 60) is False

def test_2():
    assert solution.is_obtuse(120, 30) is True

def test_3():
    assert solution.is_obtuse(90, 45) is False

def test_4():
    assert solution.is_obtuse(80, 60) is False

def test_5():
    assert solution.is_obtuse(30, 30) is True
