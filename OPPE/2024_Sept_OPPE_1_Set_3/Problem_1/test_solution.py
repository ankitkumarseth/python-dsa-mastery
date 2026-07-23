import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.div_by_exactly_one(20, 5, 6) is True

def test_2():
    assert solution.div_by_exactly_one(20, 5, 10) is False

def test_3():
    assert solution.div_by_exactly_one(25, 5, 4) is True
