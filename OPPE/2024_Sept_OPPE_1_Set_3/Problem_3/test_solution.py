import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    d = {'x': 2, 'y': 3, 'z': 4}
    solution.increment_value_with_max_limit(d, 'y', 4, 10)
    assert d == {'x': 2, 'y': 7, 'z': 4}

def test_2():
    d = {'a': 2, 'b': 5}
    solution.increment_value_with_max_limit(d, 'a', 6, 5)
    assert d == {'a': 5, 'b': 5}

def test_3():
    d = {'mango': 5, 'orange': 2}
    solution.increment_value_with_max_limit(d, 'orange', 6, 6)
    assert d == {'mango': 5, 'orange': 6}
