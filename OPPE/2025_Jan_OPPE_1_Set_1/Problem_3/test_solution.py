import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    list1 = ["name", "age", "city"]
    list2 = ["Alice", 25, "New York"]
    assert solution.make_dict_from_elems_in_index(list1, list2, 1) == {"age": 25}
    assert solution.make_dict_from_elems_in_index(list1, list2, 2) == {"city": "New York"}

def test_2():
    list1 = ["Country"]
    list2 = ["India"]
    assert solution.make_dict_from_elems_in_index(list1, list2, 0) == {"Country": "India"}

def test_3():
    list1 = ["apple", "banana", "cherry"]
    list2 = ["red", "yellow", "dark red", "yellow"]
    assert solution.make_dict_from_elems_in_index(list1, list2, 2) == {"cherry": "dark red"}
    assert solution.make_dict_from_elems_in_index(list1, list2, -3) == {"apple": "yellow"}

# Extra private tests
def test_private():
    assert solution.make_dict_from_elems_in_index(['a', 'b'], [1, 2], -1) == {'b': 2}
