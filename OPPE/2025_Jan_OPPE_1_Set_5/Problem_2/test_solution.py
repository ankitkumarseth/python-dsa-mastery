import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.next_roll_no("23f2000001") == "23f2000002"

def test_2():
    assert solution.next_roll_no("23f2004999") == "23f2005000"

def test_3():
    assert solution.next_roll_no("22f1999998") == "22f1999999"

def test_4():
    assert solution.next_roll_no("21f1000000") == "21f1000001"
