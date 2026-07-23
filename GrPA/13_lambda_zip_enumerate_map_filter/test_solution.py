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

def has_comprehensions(func):
    source = inspect.getsource(func)
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
            return True
    return False

def test_is_greater_than_5():
    assert not has_if_or_loops(solution.is_greater_than_5)
    assert not has_comprehensions(solution.is_greater_than_5)
    assert solution.is_greater_than_5([3, 4, 5, 6, 7]) == [False, False, False, True, True]

def test_filter_less_than_5():
    assert not has_if_or_loops(solution.filter_less_than_5)
    assert not has_comprehensions(solution.filter_less_than_5)
    assert solution.filter_less_than_5([3, 4, 5, 6, 7]) == [3, 4]

def test_sum_of_two_digit_numbers():
    assert not has_if_or_loops(solution.sum_of_two_digit_numbers)
    assert not has_comprehensions(solution.sum_of_two_digit_numbers)
    assert solution.sum_of_two_digit_numbers([8, 9, 10, 11, 12]) == 33
    # Edge case: negatives
    assert solution.sum_of_two_digit_numbers([5, -10, -99, -100, 20]) == -89

def test_is_all_has_a():
    assert not has_if_or_loops(solution.is_all_has_a)
    assert not has_comprehensions(solution.is_all_has_a)
    assert solution.is_all_has_a(["Apple", "Orange", "Banana"]) is True
    assert solution.is_all_has_a(["Apple", "Orange", "Kiwi"]) is False

def test_print_with_numbering(capsys):
    solution.print_with_numbering(["Apple", "Orange", "Banana"])
    captured = capsys.readouterr()
    expected = "1. Apple\n2. Orange\n3. Banana\n"
    assert captured.out == expected

def test_parallel_print(capsys):
    countries = ["United States", "Brazil", "Nigeria", "India", "Australia"]
    capitals = ["Washington, D.C.", "Brasilia", "Abuja", "New Delhi", "Canberra"]
    solution.parallel_print(countries, capitals)
    captured = capsys.readouterr()
    expected = (
        "United States - Washington, D.C.\n"
        "Brazil - Brasilia\n"
        "Nigeria - Abuja\n"
        "India - New Delhi\n"
        "Australia - Canberra\n"
    )
    assert captured.out == expected

def test_make_dict():
    assert solution.make_dict("abcd", [1, 2, 3, 4]) == {'a': 1, 'b': 2, 'c': 3, 'd': 4}

def test_indices_of_big_words():
    assert not has_if_or_loops(solution.indices_of_big_words)
    assert not has_comprehensions(solution.indices_of_big_words)
    assert solution.indices_of_big_words(["Apple", "Banana", "Orange", "Kiwi", "Cherry"]) == [1, 2, 4]

def test_decode_rle():
    assert not has_if_or_loops(solution.decode_rle)
    assert not has_comprehensions(solution.decode_rle)
    assert solution.decode_rle("abcd", [2, 4, 3, 1]) == "aabbbbcccd"
