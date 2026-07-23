import os
import sys
import pytest
from io import StringIO

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def run_test(input_data):
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO(input_data)
    sys.stdout = StringIO()
    try:
        solution.solve()
        return sys.stdout.getvalue().rstrip('\n')
    finally:
        sys.stdin = old_stdin
        sys.stdout = old_stdout

def test_1():
    input_data = "Myths gym\n"
    expected = "Myths(0) gym(0)"
    assert run_test(input_data) == expected

def test_2():
    input_data = "AEIOU aeiou\n"
    expected = "AEIOU(5) aeiou(5)"
    assert run_test(input_data) == expected

def test_3():
    input_data = "Hi! How are you?\n"
    expected = "Hi!(1) How(1) are(2) you?(2)"
    assert run_test(input_data) == expected

# Extra private tests
def test_private():
    input_data = "  a  b   c\n"
    expected = "  a(1)  b(0)   c(0)"
    assert run_test(input_data) == expected
