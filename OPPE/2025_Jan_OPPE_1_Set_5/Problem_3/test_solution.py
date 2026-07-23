import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.has_no_vowels_in_even_indices("babebibobu") is True

def test_2():
    assert solution.has_no_vowels_in_even_indices("abcde") is False

def test_3():
    assert solution.has_no_vowels_in_even_indices("test") is True

def test_4():
    assert solution.has_no_vowels_in_even_indices("bababaab") is False

def test_private():
    assert solution.has_no_vowels_in_even_indices("") is True
    assert solution.has_no_vowels_in_even_indices("AaBbCc") is False
