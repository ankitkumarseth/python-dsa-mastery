import os
import pytest
from utils.code_inspectors import assert_no_for_loops_in_file, assert_no_while_loops_in_file

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

# Import the functions from the solution file dynamically
import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_ast_no_loops():
    assert_no_for_loops_in_file(SOLUTION_FILE)
    assert_no_while_loops_in_file(SOLUTION_FILE)

def test_list_mutating_operations(capsys):
    result = solution.list_mutating_operations(["Apple", "Cherry", "Banana", "Grapes"], "Blueberry", "Apple")

    # Check returned tuple
    assert result == (['Cherry', 'Blueberry', None], "Grapes")

    # Check stdout
    captured = capsys.readouterr().out
    expected_out = (
        "sorted: ['Apple', 'Banana', 'Cherry', 'Grapes']\n"
        "append: ['Apple', 'Banana', 'Cherry', 'Grapes', 'Blueberry']\n"
        "insert: ['Apple', 'Banana', 'Cherry', 'Apple', 'Grapes', 'Blueberry']\n"
        "extend: ['Apple', 'Banana', 'Cherry', 'Apple', 'Grapes', 'Blueberry', 'Apple', 'Banana', 'Cherry']\n"
        "pop: ['Apple', 'Banana', 'Cherry', 'Apple', 'Blueberry', 'Apple', 'Banana', 'Cherry']\n"
        "remove: ['Banana', 'Cherry', 'Apple', 'Blueberry', 'Apple', 'Banana', 'Cherry']\n"
        "modify_index: ['Banana', 'Cherry', 'Apple', 'Blueberry', None, 'Banana', 'Cherry']\n"
        "modify_slice: [None, 'Cherry', None, 'Blueberry', None, 'Banana', None]\n"
        "delete_index: [None, 'Cherry', None, 'Blueberry', 'Banana', None]\n"
        "delete_slice: ['Cherry', 'Blueberry', None]\n"
    )
    assert captured == expected_out

def test_list_mutating_operations_inplace():
    original = ["Apple", "Cherry", "Banana", "Grapes"]
    ref_copy = original
    result = solution.list_mutating_operations(original, "Blueberry", "Apple")[0]

    # Check that the list object itself was mutated (inplace=True)
    assert id(original) == id(result)
    assert result == ['Cherry', 'Blueberry', None]

def test_list_non_mutating_operations(capsys):
    result = solution.list_non_mutating_operations(["Apple","Cherry","Banana", "Grapes", 'Orange', 'Pineapple'], "Blueberry","Apple")

    assert result == ["Apple","Cherry","Banana", "Grapes", 'Orange','Pineapple']

    captured = capsys.readouterr().out
    expected_out = (
        "sorted: ['Apple', 'Banana', 'Cherry', 'Grapes', 'Orange', 'Pineapple']\n"
        "append: ['Apple', 'Cherry', 'Banana', 'Grapes', 'Orange', 'Pineapple', 'Blueberry']\n"
        "insert: ['Apple', 'Cherry', 'Banana', 'Apple', 'Grapes', 'Orange', 'Pineapple']\n"
        "extend: ['Apple', 'Cherry', 'Banana', 'Grapes', 'Orange', 'Pineapple', 'Apple', 'Cherry', 'Banana']\n"
        "pop: ['Apple', 'Cherry', 'Banana', 'Grapes', 'Pineapple']\n"
        "remove: ['Cherry', 'Banana', 'Grapes', 'Orange', 'Pineapple']\n"
        "modify_index: ['Apple', 'Cherry', 'Banana', None, 'Orange', 'Pineapple']\n"
        "modify_slice: [None, 'Cherry', None, 'Grapes', None, 'Pineapple']\n"
        "delete_slice: ['Cherry', 'Grapes', 'Pineapple']\n"
    )
    assert captured == expected_out

def test_list_non_mutating_operations_inplace():
    original = ["Apple", "Cherry", "Banana", "Grapes", 'Orange','Pineapple']
    original_copy = original.copy()

    result = solution.list_non_mutating_operations(original, "Blueberry", "Apple")

    # Check that the original list was not modified (inplace=False)
    assert original == original_copy
    assert id(original) == id(result) # returns items, which is the same original list

def test_do_set_operation(capsys):
    result = solution.do_set_operation({1,2,3,4}, {3,4,5,6}, {1,2,5,6,7,8}, 5, 3)

    assert result[1:] == ([3, 4], [3, 4, 5, 6], [1, 2, 5, 6, 7, 8])

    captured = capsys.readouterr().out
    expected_out = (
        "[1, 2, 3, 4, 5]\n"
        "[1, 2, 4, 5]\n"
        "[1, 2, 3, 4, 5, 6]\n"
        "[3, 4]\n"
        "[5, 6]\n"
        "[1, 2, 3, 4, 5, 6, 7, 8]\n"
        "[3, 4]\n"
        "[1, 2, 3, 4, 7, 8]\n"
    )
    assert captured == expected_out

def test_do_set_operation_inplace():
    original = {1,2,3,4}
    result = solution.do_set_operation(original, {3,4,5,6}, {1,2,5,6,7,8}, 5, 3)[0]

    assert original == {3, 4}
    assert id(original) == id(result)
