import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.merge_and_remove_duplicates([1, 2, 3], [3, 4, 5]) == {1, 2, 3, 4, 5}

def test_2():
    assert solution.merge_and_remove_duplicates([10, 20], [30, 20, 40]) == {10, 20, 30, 40}

def test_3():
    assert solution.merge_and_remove_duplicates([1, 2], []) == {1, 2}

def test_4():
    assert solution.merge_and_remove_duplicates([], [1, 2, 3]) == {1, 2, 3}
