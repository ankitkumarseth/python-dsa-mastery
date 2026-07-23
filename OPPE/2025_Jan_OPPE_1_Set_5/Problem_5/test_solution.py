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
    input_data = "5\nchoice a a\nrange 1.5..1.8 1.6\nrange 1..2 2\nrange 3.5..4.5 4.9\nchoice b c\n"
    expected = "8\n3"
    assert run_test(input_data) == expected

def test_2():
    input_data = "3\nchoice b a\nrange 2..5 6\nchoice a c\n"
    expected = "-2\n0"
    assert run_test(input_data) == expected

def test_3():
    input_data = "4\nchoice a b\nrange 1..4 3\nchoice b b\nrange 1.1..4.5 5\n"
    expected = "5\n2"
    assert run_test(input_data) == expected
