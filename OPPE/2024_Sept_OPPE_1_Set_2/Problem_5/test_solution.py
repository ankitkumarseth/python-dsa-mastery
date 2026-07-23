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
    input_data = "3\n1,2\n3,5\n4,3\n"
    expected = "3\n2\n7"
    assert run_test(input_data) == expected

def test_2():
    input_data = "4\n5,4\n3,6\n2,3\n1,5\n"
    expected = "9\n3\n5\n4"
    assert run_test(input_data) == expected

def test_3():
    input_data = "2\n1,8\n-1,8\n"
    expected = "9\n9"
    assert run_test(input_data) == expected
