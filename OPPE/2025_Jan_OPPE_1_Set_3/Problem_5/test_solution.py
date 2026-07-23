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
        return sys.stdout.getvalue().strip()
    finally:
        sys.stdin = old_stdin
        sys.stdout = old_stdout

def test_1():
    input_data = "3 4\n1 2 3 4\n5 6 7 8\n9 10 11 12\n"
    assert run_test(input_data) == "3\n24"

def test_2():
    input_data = "2 2\n1 2\n3 4\n"
    assert run_test(input_data) == "1\n6"

def test_3():
    input_data = "4 3\n1 2 3\n4 5 6\n7 8 9\n10 11 12\n"
    assert run_test(input_data) == "2\n30"

def test_private():
    # Test ties
    input_data = "2 2\n5 5\n10 10\n"
    assert run_test(input_data) == "0\n15"
