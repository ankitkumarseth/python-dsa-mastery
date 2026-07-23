import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.count_vowels_and_consonants_in_even_indices("abcdeaeiou") == (4, 1)

def test_2():
    assert solution.count_vowels_and_consonants_in_even_indices("a11bc11de11") == (2, 1)

def test_3():
    assert solution.count_vowels_and_consonants_in_even_indices("12345") == (0, 0)

def test_4():
    assert solution.count_vowels_and_consonants_in_even_indices("ABCDE") == (2, 1)
