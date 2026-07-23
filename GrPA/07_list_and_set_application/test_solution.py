import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

# Import the functions from the solution file dynamically
import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_find_min():
    assert solution.find_min([1, 2, 3, 4, -4]) == -4
    assert solution.find_min([1, -10, 3, 4, -4]) == -10
    assert solution.find_min([5]) == 5

def test_odd_increment_even_decrement_no_modify():
    original = [1, 2, 3, 4, 5, 6]
    ref_copy = original.copy()

    result = solution.odd_increment_even_decrement_no_modify(original)

    # Check it works
    assert result == [2, 1, 4, 3, 6, 5]
    # Check it did NOT mutate
    assert original == ref_copy
    assert id(original) != id(result)

def test_odd_square_even_double_modify():
    original = [1, 2, 3, 4, 5, 6]

    result = solution.odd_square_even_double_modify(original)

    # Check it works
    assert result == [1, 4, 9, 8, 25, 12]
    # Check it DID mutate
    assert original == [1, 4, 9, 8, 25, 12]
    assert id(original) == id(result)

def test_more_than_two_unique_vowels():
    result = solution.more_than_two_unique_vowels("functions,are,not,complicated")
    assert result == {"complicated", "functions"}

    result2 = solution.more_than_two_unique_vowels("hello,world,sequoia")
    assert result2 == {"sequoia"}

def test_sum_of_list_of_lists():
    result = solution.sum_of_list_of_lists([
        [1, 2, 3, 4],
        [10, 20],
        [5],
    ])
    assert result == 45
    assert solution.sum_of_list_of_lists([]) == 0

def test_flatten():
    result = solution.flatten([
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4]
    ])
    assert result == [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
    assert solution.flatten([[], [], []]) == []

def test_all_common():
    result = solution.all_common([
        "abcde",
        "bcdef",
        "cdefg",
    ])
    assert result == "cde"

    result2 = solution.all_common(["hello", "world"])
    assert result2 == "lo" # wait, h,e,l,o and w,o,r,l,d -> l,o -> sorted -> "lo"

def test_vocabulary():
    result = solution.vocabulary([
        "This is a car",
        "He is playing with a bat",
        "He and she are playing",
    ])
    assert result == {'a', 'and', 'are', 'bat', 'car', 'he', 'is', 'playing', 'she', 'this', 'with'}
