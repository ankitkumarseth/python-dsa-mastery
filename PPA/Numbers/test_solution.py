import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_percentage_increased():
    assert round(solution.percentage_increased(50, 75)) == 50
    assert round(solution.percentage_increased(80, 100)) == 25
    assert round(solution.percentage_increased(80, 80)) == 0

    # Edge case: Floating point input
    assert round(solution.percentage_increased(50.5, 75.75)) == 50
    # Edge case: original is 0
    assert solution.percentage_increased(0, 0) == 0.0

def test_is_ten_digit_even():
    assert solution.is_ten_digit_even(8769473839) is False
    assert solution.is_ten_digit_even(9289479278) is True
    assert solution.is_ten_digit_even(87694) is False
    assert solution.is_ten_digit_even(928947) is False
    assert solution.is_ten_digit_even(-9289428942) is True
    assert solution.is_ten_digit_even(9289428942) is True

    # Edge case: 10-digit number but negative and odd
    assert solution.is_ten_digit_even(-9289428941) is False
    # Edge case: Exactly 9 digits (max 9-digit)
    assert solution.is_ten_digit_even(999999999) is False
    # Edge case: Exactly 11 digits (min 11-digit)
    assert solution.is_ten_digit_even(10000000000) is False

def test_arithmetic_operations():
    assert solution.arithmetic_operations((1, 2)) == (3, -1, 2, 0)
    assert solution.arithmetic_operations((10, 5)) == (15, 5, 50, 2)
    assert solution.arithmetic_operations((-1, 1)) == (0, -2, -1, -1)

    # Edge case: 0 division (if b == 0 it should probably raise ZeroDivisionError naturally)
    with pytest.raises(ZeroDivisionError):
        solution.arithmetic_operations((10, 0))

    # Edge case: Negative division flooring check
    # -5 // 2 == -3
    assert solution.arithmetic_operations((-5, 2)) == (-3, -7, -10, -3)
