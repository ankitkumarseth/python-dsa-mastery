import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_percentage_increase():
    assert solution.percentage_increase(50, 75) == 50.0
    assert solution.percentage_increase(80, 100) == 25.0

def test_is_ten_digit_even():
    assert solution.is_ten_digit_even(8769473839) is False
    assert solution.is_ten_digit_even(9289479278) is True

def test_find_indices_of_element():
    assert solution.find_indices_of_element([1, 2, 3, 2, 4], 2) == [1, 3]
    assert solution.find_indices_of_element(['a', 'b', 'a', 'c'], 'a') == [0, 2]

def test_swap_adjacent_elements():
    assert solution.swap_adjacent_elements((1, 2, 3, 4, 5, 6)) == (2, 1, 4, 3, 6, 5)
    assert solution.swap_adjacent_elements(('a', 'b', 'c', 'd')) == ('b', 'a', 'd', 'c')

def test_common_chars():
    assert solution.common_chars('apple', 'ball') == 'al'
    assert solution.common_chars('abcde', 'edfci') == 'cde'

def test_count_values_occurrences():
    assert solution.count_values_occurrences({'a': 1, 'b': 2, 'c': 1}) == {1: 2, 2: 1}
    assert solution.count_values_occurrences({1: 'x', 2: 'y', 3: 'x'}) == {'x': 2, 'y': 1}
