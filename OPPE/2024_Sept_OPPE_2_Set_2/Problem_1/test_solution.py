import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.sum_of_floored_to_tens(35, 46) == 70

def test_2():
    assert solution.sum_of_floored_to_tens(12, 7) == 10

def test_3():
    assert solution.sum_of_floored_to_tens(135, 265) == 390
