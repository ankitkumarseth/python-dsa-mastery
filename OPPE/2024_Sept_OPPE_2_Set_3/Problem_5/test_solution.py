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
    input_data = "5\n11 45\n12 47\n13 78\n14 69\n15 50\n"
    expected = "13 80\n14 70"
    assert run_test(input_data) == expected

def test_2():
    input_data = "3\n11 55\n12 35\n13 69\n"
    expected = "13 70"
    assert run_test(input_data) == expected

def test_3():
    input_data = "4\n21 88\n22 89\n23 90\n24 70\n"
    expected = "21 90\n22 90"
    assert run_test(input_data) == expected
