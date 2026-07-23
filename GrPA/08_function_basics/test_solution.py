import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

# Import the functions from the solution file dynamically
import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)


def test_swap_halves():
    assert solution.swap_halves((1,2,3,4,5,6)) == (4,5,6,1,2,3)
    assert solution.swap_halves((9,8,7,6,5,4)) == (6,5,4,9,8,7)

def test_swap_at_index():
    assert solution.swap_at_index((1,2,3,4,5,6), 1) == (3,4,5,6,1,2)
    assert solution.swap_at_index((1,2,3,4,5,6), 0) == (2,3,4,5,6,1)

def test_rotate_k():
    assert solution.rotate_k((1,2,3,4,5,6), 4) == (3,4,5,6,1,2)
    assert solution.rotate_k((1,2,3,4,5,6), 11) == (2,3,4,5,6,1)
    assert solution.rotate_k((1,2,3), 0) == (1,2,3)

def test_first_and_last_index():
    assert solution.first_and_last_index((1,2,3,1,5,6), 1) == (0,3)
    assert solution.first_and_last_index((0,2,1,4,5,6), 1) == (2,2)

def test_reverse_first_and_last_halves():
    original = [1,2,3,4,5,6,7,8]
    solution.reverse_first_and_last_halves(original)

    assert original == [4,3,2,1,8,7,6,5]
