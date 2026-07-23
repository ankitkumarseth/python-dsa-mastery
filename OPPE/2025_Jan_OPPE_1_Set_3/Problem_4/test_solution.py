import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.replace_vowels_with_next_alphabet("Toyota") == "Tpyptb"

def test_2():
    assert solution.replace_vowels_with_next_alphabet("HONDA") == "HPNDB"

def test_3():
    assert solution.replace_vowels_with_next_alphabet("Tesla") == "Tfslb"

def test_4():
    assert solution.replace_vowels_with_next_alphabet("BMW") == "BMW"

def test_5():
    assert solution.replace_vowels_with_next_alphabet("Volkswagen") == "Vplkswbgfn"

def test_private():
    assert solution.replace_vowels_with_next_alphabet("aeiouAEIOU") == "bfjpvBFJPV"
