import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    data = {
        "Alice": [90, 80, 85],
        "Bob": [40, 50, 60],
        "Charlie": [30, 40, 20], 
        "Ram": [78, 92, 85, 79, 81],
        "Babu": [67, 70, 75],
        "Kumar": [100, 100, 100, 100, 100, 100, 40]
    }
    assert solution.filter_students(data, 'excellent') == {'Alice', 'Kumar'}

def test_2():
    data = {
        "Alice": [90, 80, 85],
        "Bob": [40, 50, 60],
        "Charlie": [30, 40, 20], 
        "Ram": [78, 92, 85, 79, 81],
        "Babu": [67, 70, 75],
        "Kumar": [100, 100, 100, 100, 100, 100, 40]
    }
    assert solution.filter_students(data, 'good') == {'Babu', 'Bob', 'Ram'}

def test_3():
    data = {
        "Alice": [90, 80, 85],
        "Bob": [40, 50, 60],
        "Charlie": [30, 40, 20], 
        "Ram": [78, 92, 85, 79, 81],
        "Babu": [67, 70, 75],
        "Kumar": [100, 100, 100, 100, 100, 100, 40]
    }
    assert solution.filter_students(data, 'all_pass') == {'Alice', 'Babu', 'Ram'}

def test_4():
    data = {
        "Alice": [90, 80, 85],
        "Bob": [40, 50, 60],
        "Charlie": [30, 40, 20], 
        "Ram": [78, 92, 85, 79, 81],
        "Babu": [67, 70, 75],
        "Kumar": [100, 100, 100, 100, 100, 100, 40]
    }
    assert solution.filter_students(data, 'balanced') == {'Alice', 'Babu'}

# Extra private tests
def test_private():
    data = {}
    assert solution.filter_students(data, 'excellent') == set()
    data = {"X": [85]}
    assert solution.filter_students(data, 'excellent') == {'X'}
    assert solution.filter_students(data, 'good') == set()
