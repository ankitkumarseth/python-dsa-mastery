import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    sentence = 'This is a Test sEnteEnce'
    assert solution.last_word_starts_with_upper_case(sentence) == 'Test'

def test_2():
    sentence = 'no uppeRcase wOrds here'
    assert solution.last_word_starts_with_upper_case(sentence) is None

def test_3():
    sentence = 'NO uppeRcase wOrds here'
    assert solution.last_word_starts_with_upper_case(sentence) == 'NO'

def test_4():
    sentence = 'Whishing you ALL the beSt'
    assert solution.last_word_starts_with_upper_case(sentence) == 'ALL'
