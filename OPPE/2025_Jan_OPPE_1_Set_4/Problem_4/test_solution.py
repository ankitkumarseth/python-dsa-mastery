import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.first_non_repeating_char("abcab") == "c"

def test_2():
    assert solution.first_non_repeating_char("aabbcc") is None
    assert solution.first_non_repeating_char("aabbccd") == 'd'

def test_3():
    assert solution.first_non_repeating_char("buzzingbee") == "u"

def test_private():
    assert solution.first_non_repeating_char("") is None
    assert solution.first_non_repeating_char("a") == "a"
