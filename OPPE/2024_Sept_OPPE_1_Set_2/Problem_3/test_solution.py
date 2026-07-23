import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.replace_middle_with_n_times_middle((1, 2, 3, 4, 5), 5) == (1, 2, 3, 3, 3, 3, 3, 4, 5)

def test_2():
    assert solution.replace_middle_with_n_times_middle((1, 2, 3), 4) == (1, 2, 2, 2, 2, 3)

def test_3():
    assert solution.replace_middle_with_n_times_middle((7, 8, 9), 3) == (7, 8, 8, 8, 9)
