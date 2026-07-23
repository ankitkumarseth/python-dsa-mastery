import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.mm_dd_yy_to_yy_dd_mm("12-25-21") == "21-25-12"

def test_2():
    assert solution.mm_dd_yy_to_yy_dd_mm("01-01-00") == "00-01-01"

def test_3():
    assert solution.mm_dd_yy_to_yy_dd_mm("10-31-99") == "99-31-10"
