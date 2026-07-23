import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.deinterleave("abcdef") == "acebdf"

def test_2():
    assert solution.deinterleave("12345") == "13524"

def test_3():
    assert solution.deinterleave("helloworld") == "hloolelwrd"

# Extra private tests
def test_private():
    assert solution.deinterleave("") == ""
    assert solution.deinterleave("a") == "a"
    assert solution.deinterleave("ab") == "ab"
