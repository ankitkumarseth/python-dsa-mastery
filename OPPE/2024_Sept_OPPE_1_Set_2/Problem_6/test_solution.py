import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    M = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert solution.walk_matrix(M, 'L') == [1, 4, 7, 8, 9]

def test_2():
    M = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15]
    ]
    assert solution.walk_matrix(M, 'Z') == [0, 1, 2, 3, 6, 9, 12, 13, 14, 15]

def test_3():
    M = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert solution.walk_matrix(M, 'O') == [1, 2, 3, 6, 9, 8, 7, 4]
