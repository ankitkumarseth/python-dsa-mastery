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
    """Check if the function's AST contains If, For, or While statements.
    (Comprehensions are allowed and will not trigger this)."""
    source = inspect.getsource(func)
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, (ast.If, ast.For, ast.While, ast.AsyncFor, ast.AsyncFunctionDef)):
            return True
    return False

def test_sum_of_squares():
    assert not has_if_or_loops(solution.sum_of_squares)
    assert solution.sum_of_squares([1, 2, 3, 4]) == 30
    assert solution.sum_of_squares([0, -1]) == 1

def test_total_cost():
    assert not has_if_or_loops(solution.total_cost)
    assert solution.total_cost([(1, 2), (3, 4), (1, 5)]) == 19
    assert solution.total_cost([]) == 0

def test_abbreviation():
    assert not has_if_or_loops(solution.abbreviation)
    assert solution.abbreviation("ordinary wizarding levels") == "O.W.L."
    assert solution.abbreviation("hello world") == "H.W."

def test_palindromes():
    assert not has_if_or_loops(solution.palindromes)
    assert solution.palindromes(["moon", "noon", "dad", "dog", "cat", "madam"]) == ["noon", "dad", "madam"]
    assert solution.palindromes(["a", "abc", "aba"]) == ["a", "aba"]

def test_all_chars_from_big_words():
    assert not has_if_or_loops(solution.all_chars_from_big_words)
    result = solution.all_chars_from_big_words("List comprehensions are a good start for functional programming")
    expected = {'a', 'c', 'e', 'f', 'g', 'h', 'i', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u'}
    assert result == expected

def test_flatten():
    assert not has_if_or_loops(solution.flatten)
    assert solution.flatten([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]) == [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
    assert solution.flatten([[], [1], []]) == [1]

def test_unflatten():
    assert not has_if_or_loops(solution.unflatten)
    result = solution.unflatten([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4], 3)
    assert result == [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

def test_make_identity_matrix():
    assert not has_if_or_loops(solution.make_identity_matrix)
    result = solution.make_identity_matrix(3)
    assert result == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert solution.make_identity_matrix(1) == [[1]]

def test_make_lower_triangular_matrix():
    assert not has_if_or_loops(solution.make_lower_triangular_matrix)
    result = solution.make_lower_triangular_matrix(3)
    assert result == [[1, 0, 0], [1, 2, 0], [1, 2, 3]]
    assert solution.make_lower_triangular_matrix(1) == [[1]]
