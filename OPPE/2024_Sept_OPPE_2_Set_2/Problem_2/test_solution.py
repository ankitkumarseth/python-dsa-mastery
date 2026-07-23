import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.surround_first_two_and_last_two_with_brackets("hello") == "[he]l[lo]"

def test_2():
    assert solution.surround_first_two_and_last_two_with_brackets("python") == "[py]th[on]"

def test_3():
    assert solution.surround_first_two_and_last_two_with_brackets("warrior") == "[wa]rri[or]"

def test_4():
    assert solution.surround_first_two_and_last_two_with_brackets("four") == "[fo][ur]"
