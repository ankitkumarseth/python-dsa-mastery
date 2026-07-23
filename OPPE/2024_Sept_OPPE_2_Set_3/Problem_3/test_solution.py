import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    d = {"first": "apple", "second": "mango", "third": "banana"}
    solution.swap_last_chars_of_values(d, "first", "second")
    assert d == {"first": "applo", "second": "mange", "third": "banana"}

def test_2():
    d = {"key1": "hello", "key2": "world"}
    solution.swap_last_chars_of_values(d, "key1", "key2")
    assert d == {"key1": "helld", "key2": "worlo"}

def test_3():
    d = {"a": "day", "b": "play", "c": "stay"}
    solution.swap_last_chars_of_values(d, "a", "b")
    assert d == {"a": "day", "b": "play", "c": "stay"}
    
    d2 = {"a": "day", "b": "flat", "c": "stay"}
    solution.swap_last_chars_of_values(d2, "a", "b")
    assert d2 == {"a": "dat", "b": "flay", "c": "stay"}
