import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.difference([1, 2, 3, 4, 5, 6]) == [1, 1, 1, 1, 1]
    assert solution.difference([1, 1, 2, 3, 5, 8, 13]) == [0, 1, 1, 2, 3, 5]
    assert solution.difference([1, 10, 20, 10, 10]) == [9, 10, -10, 0]

def test_2():
    l = [1, 5, 15, 35, 70, 126, 210, 330, 495, 715]
    assert solution.nth_order_difference(l, 1) == [4, 10, 20, 35, 56, 84, 120, 165, 220]
    assert solution.nth_order_difference(l, 2) == [6, 10, 15, 21, 28, 36, 45, 55]
    assert solution.nth_order_difference(l, 3) == [4, 5, 6, 7, 8, 9, 10]
    assert solution.nth_order_difference(l, 4) == [1, 1, 1, 1, 1, 1]

def test_3():
    assert solution.has_positive_trend([1, 3, 5, 7, 9]) is True
    assert solution.has_positive_trend([10, 8, 6, 4, 2]) is False
    assert solution.has_positive_trend([1, 2, 1, 0, -1]) is False

def test_4():
    assert solution.moving_average([1, 2, 3, 4, 5], 2) == [1.5, 2.5, 3.5, 4.5]
    assert solution.moving_average([10, 12, 8, 10, 6, 8, 4], 3) == [10.0, 10.0, 8.0, 8.0, 6.0]

def test_5():
    assert solution.has_negative_average_trend([1, 2, 3, 4, 5], 3) is False
    assert solution.has_negative_average_trend([10, 8, 6, 4, 2], 2) is True
    assert solution.has_negative_average_trend([1, 0, 3, 1, 5, 3, 8], 3) is False
    assert solution.has_negative_average_trend([10, 12, 8, 10, 6, 8, 4], 3) is True
