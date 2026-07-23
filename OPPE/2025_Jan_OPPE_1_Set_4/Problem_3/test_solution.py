import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.remove_n_elems_from_index((1, 2, 3, 4, 5), 2, 1) == (1, 4, 5)

def test_2():
    assert solution.remove_n_elems_from_index((10, 20, 30, 40, 50), 3, 2) == (10, 20)

def test_3():
    assert solution.remove_n_elems_from_index((1, 2, 3, 4, 5), 5, 0) == ()
    assert solution.remove_n_elems_from_index((1, 2, 3, 4, 5), 0, 5) == (1, 2, 3, 4, 5)
    
def test_private():
    assert solution.remove_n_elems_from_index((1, 2, 3), 10, 0) == () # more than length
    assert solution.remove_n_elems_from_index((1, 2, 3), 1, 10) == (1, 2, 3) # out of bounds
