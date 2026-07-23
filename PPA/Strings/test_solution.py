import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_format_as_second_comma_first():
    assert solution.format_as_second_comma_first(('hello', 'python')) == 'python, hello'
    assert solution.format_as_second_comma_first((1, 2)) == '2, 1'
    assert solution.format_as_second_comma_first((1.2, 3.4)) == '3.4, 1.2'

    # Edge case: tuple with mixed data types
    assert solution.format_as_second_comma_first((None, [1, 2])) == '[1, 2], None'

def test_even_first_odd_reversed():
    assert solution.even_first_odd_reversed('abcde') == 'acedb'
    assert solution.even_first_odd_reversed('python') == 'ptonhy'
    assert solution.even_first_odd_reversed('abracadabra') == 'arcdbaraaab'

    # Edge case: Empty string
    assert solution.even_first_odd_reversed('') == ''

    # Edge case: Single character string
    assert solution.even_first_odd_reversed('A') == 'A'

    # Edge case: Two character string
    assert solution.even_first_odd_reversed('AB') == 'AB'

def test_is_palindrome():
    assert solution.is_palindrome(121) is True
    assert solution.is_palindrome(123) is False
    assert solution.is_palindrome(-121) is False

    # Edge case: Single digit number is always a palindrome
    assert solution.is_palindrome(7) is True
    assert solution.is_palindrome(0) is True

    # Edge case: Multi-digit zero ends
    assert solution.is_palindrome(10) is False
