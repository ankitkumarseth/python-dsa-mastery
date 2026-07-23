import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.count_odd_three_digit_nums([101, -203, None, 99, 300]) == 2

def test_2():
    assert solution.count_odd_three_digit_nums([None, 120, 301, -401, 78]) == 2

def test_3():
    assert solution.count_odd_three_digit_nums([10, 305, 507, 99]) == 2
