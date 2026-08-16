import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_is_three_digit_and_digit_sum_divisible_by_k():
    assert solution.is_three_digit_and_digit_sum_divisible_by_k(145, 5) is True
    assert solution.is_three_digit_and_digit_sum_divisible_by_k(123, 5) is False
    assert solution.is_three_digit_and_digit_sum_divisible_by_k(12, 5) is False
    assert solution.is_three_digit_and_digit_sum_divisible_by_k(450, 10) is False
    assert solution.is_three_digit_and_digit_sum_divisible_by_k(999, 9) is True
    assert solution.is_three_digit_and_digit_sum_divisible_by_k(99, 9) is False
    assert solution.is_three_digit_and_digit_sum_divisible_by_k(1040, 5) is False
    assert solution.is_three_digit_and_digit_sum_divisible_by_k(756, 6) is True
    assert solution.is_three_digit_and_digit_sum_divisible_by_k(321, 4) is False
    assert solution.is_three_digit_and_digit_sum_divisible_by_k(1, 8) is False
