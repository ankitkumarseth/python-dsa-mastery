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
    input_data = "5\napple\norange\npineapple\nmango\nkiwi\n"
    expected = "egnaro\napple\nognam\npineapple\niwik"
    assert run_test(input_data) == expected

def test_2():
    input_data = "4\npython\njava\njavascript\nrust\n"
    expected = "avaj\npython\ntsur\njavascript"
    assert run_test(input_data) == expected

def test_3():
    input_data = "6\nharry\nron\nhermione\ndraco\nneville\nhagrid\n"
    expected = "nor\nharry\nocard\nhermione\ndirgah\nneville"
    assert run_test(input_data) == expected
