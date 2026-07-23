import os
import ast
import inspect
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def has_if_or_loops(func):
    source = inspect.getsource(func)
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, (ast.If, ast.For, ast.While, ast.AsyncFor, ast.AsyncFunctionDef)):
            return True
    return False

def test_total_price():
    result = solution.total_price(
        {'Apple': 2.0, 'Banana': 3.0, 'Orange': 4.0, 'Grapes': 3.0, 'Papaya': 5.0},
        [("Apple", 3), ("Orange", 5), ("Grapes", 4)]
    )
    assert result == 38.0

    # Edge case: empty purchases
    assert solution.total_price({'Apple': 2.0}, []) == 0.0

def test_total_price_no_loops():
    assert not has_if_or_loops(solution.total_price_no_loops)
    result = solution.total_price_no_loops(
        {'Apple': 2.0, 'Banana': 3.0, 'Orange': 4.0, 'Grapes': 3.0, 'Papaya': 5.0},
        [("Apple", 3), ("Orange", 5), ("Grapes", 4)]
    )
    assert result == 38.0

def test_find_cheapest_fruit():
    result = solution.find_cheapest_fruit({'Apple': 7, 'Banana': 3, 'Orange': 4, 'Grapes': 6, 'Papaya': 5})
    assert result == "Banana"

    # Edge case: multiple minimums, find first
    result_tie = solution.find_cheapest_fruit({'Apple': 7, 'Banana': 2, 'Orange': 4, 'Pear': 2})
    assert result_tie in ["Banana", "Pear"]

def test_find_cheapest_fruit_no_loops():
    assert not has_if_or_loops(solution.find_cheapest_fruit_no_loops)
    result = solution.find_cheapest_fruit_no_loops({'Apple': 7, 'Banana': 3, 'Orange': 4, 'Grapes': 6, 'Papaya': 5})
    assert result == "Banana"

def test_group_fruits():
    result = solution.group_fruits([
        "Avocado", "Apple", "Banana",
        "Blackberry", "Cherry", "Cranberry",
        "Grape", "Mango"
    ])
    expected = {
        "A": ["Apple", "Avocado"],
        "B": ["Banana", "Blackberry"],
        "C": ["Cherry", "Cranberry"],
        "G": ["Grape"],
        "M": ["Mango"]
    }
    assert result == expected
    assert solution.group_fruits([]) == {}

def test_bin_fruits():
    result = solution.bin_fruits({'Apple': 7, 'Banana': 3, 'Orange': 4, 'Grapes': 6, 'Papaya': 5, 'Mango': 2, 'Amla': 1, 'Jackfruit': 10})
    expected = {
        "cheap": {'Amla', 'Mango'},
        "affordable": {'Banana', 'Grapes', 'Orange', 'Papaya'},
        "costly": {'Apple', 'Jackfruit'}
    }
    assert result == expected
    assert solution.bin_fruits({}) == {"cheap": set(), "affordable": set(), "costly": set()}
