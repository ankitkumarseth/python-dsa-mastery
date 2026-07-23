import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 3, 'c': 4}
    assert solution.merge_dictionaries(d1, d2) == {'a': 1, 'b': 5, 'c': 4}

def test_2():
    d1 = {'x': 10, 'y': 20}
    d2 = {}
    assert solution.merge_dictionaries(d1, d2) == {'x': 10, 'y': 20}

def test_3():
    d1 = {'a': 5}
    d2 = {'b': 10}
    assert solution.merge_dictionaries(d1, d2) == {'a': 5, 'b': 10}
