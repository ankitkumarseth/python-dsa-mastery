import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    l = [1, 2, 3, 4, 5]
    solution.remove_elements_at_two_indices(l, 1, 3)
    assert l == [1, 3, 5]

def test_2():
    l = [10, 20, 30, 40, 50]
    solution.remove_elements_at_two_indices(l, 0, 4)
    assert l == [20, 30, 40]

def test_3():
    l = [1, 2, 3, 4, 5, 6]
    solution.remove_elements_at_two_indices(l, 2, 4)
    assert l == [1, 2, 4, 6]
