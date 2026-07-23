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
    input_data = "2\n4\n6\nNaN\n8\nEND\n"
    expected = "2.0\n3.0\n4.0\n5.0"
    assert run_test(input_data) == expected

def test_2():
    input_data = "1\n2\n3\nNaN\n4\nNaN\nNaN\n5\nEND\n"
    expected = "1.0\n1.5\n2.0\n2.5\n3.0"
    assert run_test(input_data) == expected

def test_3():
    input_data = "10\nEND\n"
    expected = "10.0"
    assert run_test(input_data) == expected
