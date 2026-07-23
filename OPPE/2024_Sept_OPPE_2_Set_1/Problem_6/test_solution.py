import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    grocery_list = [
        {'name': 'apple', 'quantity': 2, 'price': 3},
        {'name': 'banana', 'quantity': 5, 'price': 2},
        {'name': 'carrot', 'quantity': 4, 'price': 1}
    ]
    assert solution.process_grocery_list(grocery_list, 'total_bill_amount') == 20

def test_2():
    grocery_list = [
        {'name': 'apple', 'quantity': 2, 'price': 3},
        {'name': 'banana', 'quantity': 5, 'price': 2},
        {'name': 'carrot', 'quantity': 4, 'price': 1}
    ]
    assert solution.process_grocery_list(grocery_list, 'max_quantity_item') == 'banana'
    
    grocery_list_2 = [
        {'name': 'apple', 'quantity': 2, 'price': 3},
        {'name': 'carrot', 'quantity': 6, 'price': 1},
        {'name': 'banana', 'quantity': 6, 'price': 2},
    ]
    assert solution.process_grocery_list(grocery_list_2, 'max_quantity_item') == 'carrot'

def test_3():
    grocery_list = [
        {'name': 'banana', 'quantity': 5, 'price': 2},
        {'name': 'apple', 'quantity': 2, 'price': 3},
        {'name': 'date', 'quantity': 4, 'price': 1},
        {'name': 'carrot', 'quantity': 4, 'price': 1},
    ]
    expected = [
        {'name': 'banana', 'quantity': 5, 'price': 2},
        {'name': 'apple', 'quantity': 2, 'price': 3},
        {'name': 'carrot', 'quantity': 4, 'price': 1},
        {'name': 'date', 'quantity': 4, 'price': 1},
    ]
    assert solution.process_grocery_list(grocery_list, 'sort_by_total_amount') == expected
