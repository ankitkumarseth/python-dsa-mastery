import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_rotate_list():
    assert solution.rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert solution.rotate_list(['a', 'b', 'c', 'd', 'e'], 3) == ['c', 'd', 'e', 'a', 'b']

    # Edge case: k is larger than list length
    assert solution.rotate_list([1, 2, 3], 5) == [2, 3, 1]

    # Edge case: k is 0
    assert solution.rotate_list([1, 2, 3], 0) == [1, 2, 3]

    # Edge case: k is a perfect multiple of list length
    assert solution.rotate_list([1, 2, 3], 300) == [1, 2, 3]

def test_swap_alternate_elements():
    assert solution.swap_alternate_elements((1, 2, 3, 4, 5, 6)) == (2, 1, 4, 3, 6, 5)
    assert solution.swap_alternate_elements(('a', 'b', 'c', 'd')) == ('b', 'a', 'd', 'c')
    assert solution.swap_alternate_elements(tuple("alpha1")) == tuple("lahp1a")

    # Edge case: empty tuple
    assert solution.swap_alternate_elements(()) == ()

    # Edge case: 2 element tuple
    assert solution.swap_alternate_elements((1, 2)) == (2, 1)

def test_in_exactly_one():
    assert solution.in_exactly_one([1, 2, 3], [3, 4, 5]) == {1, 2, 4, 5}
    assert solution.in_exactly_one(['apple', 'ball', 'cat'], ['ball', 'cat', 'dog']) == {'apple', 'dog'}
    assert solution.in_exactly_one(list(range(1, 10)), list(range(5, 15))) == {*range(1, 5), *range(10, 15)}

    # Edge case: identical lists
    assert solution.in_exactly_one([1, 2], [1, 2]) == set()

    # Edge case: empty lists
    assert solution.in_exactly_one([], []) == set()

def test_unique_vowels():
    assert solution.unique_vowels('aeiouApple aeiouOrange') == {'A', 'O', 'a', 'e', 'i', 'o', 'u'}
    assert solution.unique_vowels("how's the josh!!!") == {'e', 'o'}
    assert solution.unique_vowels('Ian Avinkov') == {'A', 'I', 'a', 'i', 'o'}

    # Edge case: no vowels
    assert solution.unique_vowels('myth rhythm') == set()

    # Edge case: empty string
    assert solution.unique_vowels('') == set()

def test_common_char_sorted_str():
    assert solution.common_char_sorted_str('apple', 'ball') == 'al'
    assert solution.common_char_sorted_str('abcde', 'edfci') == 'cde'
    assert solution.common_char_sorted_str('apple', 'orange') == 'ae'

    # Edge case: completely disjoint strings
    assert solution.common_char_sorted_str('abc', 'xyz') == ''

    # Edge case: exact same strings
    assert solution.common_char_sorted_str('dog', 'dog') == 'dgo'
