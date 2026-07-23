import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    data = [('101', 85), ('102', 75), ('103', 45), ('104', 95), ('105', 35)]
    assert solution.get_roll_nos(data, 'above_average') == ['101', '102', '104']
    assert solution.get_roll_nos(data, 'fail') == ['105']
    assert solution.get_roll_nos(data, 'bla-bla') is None
    assert solution.get_roll_nos(data, None) == ['101', '102', '103', '104', '105']

def test_2():
    data  = [('101', 55), ('102', 25), ('103', 40), ('104', 45), ('105', 35)]
    assert solution.get_roll_nos(data, 'fail') == ['102', '105']
    assert solution.get_roll_nos(data, 'below_average') == ['102', '105']
    assert solution.get_roll_nos(data, 'above_average') == ['101', '103', '104']

def test_3():
    data = [('101', 85), ('102', 75), ('103', 45), ('104', 95), ('105', 35)]
    assert solution.get_roll_nos(data, 'toppers') == ['104']

def test_4():
    data = [('101', 85), ('102', 75), ('103', 45), ('104', 95), ('105', 35)]
    assert solution.get_roll_nos(data) == ['101', '102', '103', '104', '105']
