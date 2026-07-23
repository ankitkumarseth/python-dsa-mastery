import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.count_unique_even_odd([]) == {"even": 0, "odd": 0}

def test_2():
    l = [2, 2, 4, 4, 6, 6]
    assert solution.count_unique_even_odd(l) == {"even": 3, "odd": 0}

def test_3():
    assert solution.count_unique_even_odd([1, 1, 1]) == {"even": 0, "odd": 1}

def test_4():
    assert solution.count_unique_even_odd([1,2,3,4,2,3,4,5,4,5,6,8,8,8]) == {"even": 4, "odd": 3}

# Extra private tests
def test_private():
    assert solution.count_unique_even_odd([0, 0, -1, -2, -2]) == {"even": 2, "odd": 1}
