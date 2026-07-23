import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.are_orthogonal((1, 2), (12, -6)) is True

def test_2():
    assert solution.are_orthogonal((2, 0), (4, 1)) is False

def test_3():
    assert solution.are_orthogonal((0, 5), (-5, 0)) is True

def test_private():
    assert solution.are_orthogonal((0, 0), (5, 5)) is True
