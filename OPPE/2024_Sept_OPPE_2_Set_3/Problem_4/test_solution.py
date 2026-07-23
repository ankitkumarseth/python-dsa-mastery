import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    sentence = "The key and the lock is there"
    assert solution.get_words_after_the(sentence) == ['key', 'lock']

def test_2():
    sentence = "The the and the The"
    assert solution.get_words_after_the(sentence) == ['the', 'and', 'The']

def test_3():
    sentence = "the quick brown fox jumps over the lazy dog"
    assert solution.get_words_after_the(sentence) == ['quick', 'lazy']
