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
    input_data = "3\n2\n1\n2\n"
    assert run_test(input_data) == "[2]"

def test_2():
    input_data = "5\n3\n5\n2\n2\n5\n"
    assert run_test(input_data) == "[2, 5]"

def test_3():
    input_data = "4\n10\n20\n5\n10\n1\n1\n20\n9\n" # wait, input format says "The next n lines each contain n numbers", but this seems to have more than 4 lines? Let's assume it reads all inputs or just n inputs. The example has 4 for n and 8 inputs. Wait, the problem says "The next n lines each contain n numbers"? That implies n lines of multiple numbers or n*n? The TCs just list integers. Let's just read until EOF or precisely parse what the test expects. Actually, "4" followed by 8 numbers means maybe n is lines, and each line has a number, wait, the example had `10` followed by 10 numbers. TC3 has `4` followed by 8 numbers! Let's just ensure the test input matches exact TC.
    assert run_test(input_data) == "[10]"
