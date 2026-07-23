import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.process_sentence("level noon civic radar something wrong", "count_words") == 6

def test_2():
    assert solution.process_sentence("level noon civic radar something wrong", "count_palindromes") == 4

def test_3():
    assert solution.process_sentence("hello world programming fun", "count_words_with_repeated_chars") == 2

def test_4():
    assert solution.process_sentence("hello world programming is fun and interesting", "words_with_max_len") == {"programming", "interesting"}
