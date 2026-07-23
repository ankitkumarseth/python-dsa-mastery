import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    words = ['walkING', 'readinG', 'wrong']
    assert solution.get_words_by_criteria(words, 'continuous') == ['walkING', 'readinG']

def test_2():
    words = ['ronoroaZORO', 'Jogging', 'entertainment', 'aeiouUIEIO', 'beautiful']
    assert solution.get_words_by_criteria(words, 'vowel_rich') == ['ronoroaZORO', 'aeiouUIEIO']

def test_3():
    words = ['StrenGth', 'hello', 'aaccddee', 'python', 'jumping', 'PsYchOloGy']
    assert solution.get_words_by_criteria(words, 'consonant_rich') == ['StrenGth', 'PsYchOloGy']

def test_4():
    words = ['abc', 'flying', 'aBcD', 'XYZxyz', 'xXYyZz', 'rythms']
    assert solution.get_words_by_criteria(words, 'sorted') == ['abc', 'aBcD', 'xXYyZz']

def test_5():
    words = ['abc', 'flying', 'aBcD', 'XYZxyz', 'xXYyZz', 'rythms']
    assert solution.get_words_by_criteria(words, 'unknown') is None
