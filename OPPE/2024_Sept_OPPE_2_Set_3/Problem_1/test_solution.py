import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.product_of_sum_and_abs_diff_of_digits(54) == 9

def test_2():
    assert solution.product_of_sum_and_abs_diff_of_digits(82) == 60

def test_3():
    assert solution.product_of_sum_and_abs_diff_of_digits(34) == 7
