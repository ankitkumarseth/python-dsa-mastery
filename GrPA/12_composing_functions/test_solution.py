import os
import pytest
import copy

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

@pytest.fixture


def get_matrix_1():
    return [
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 1, 0, 0]
    ]

@pytest.fixture


def get_matrix_2():
    return [
        [0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 1, 1]
    ]

def test_index_of_occurances():
    row = [0, 0, 1, 1, 0]
    assert solution.index_of_first_occurance(row, 1) == 2
    assert solution.index_of_last_occurance(row, 1) == 3

def test_is_valid_coordinate(get_matrix_1):
    matrix = get_matrix_1
    assert solution.is_valid_coordinate(2, 2, matrix) is True
    assert solution.is_valid_coordinate(2, 5, matrix) is False
    assert solution.is_valid_coordinate(5, -2, matrix) is False

def test_valid_adjacent_coordinates(get_matrix_1):
    matrix = get_matrix_1
    assert solution.valid_adjacent_coordinates(2, 2, matrix) == {(1, 2), (2, 1), (2, 3), (3, 2)}
    assert solution.valid_adjacent_coordinates(0, 2, matrix) == {(0, 1), (0, 3), (1, 2)}

def test_next_coordinate_with_value(get_matrix_1):
    matrix = get_matrix_1
    assert solution.next_coordinate_with_value((2, 2), 1, matrix, (2,1)) == (2, 3)
    assert solution.next_coordinate_with_value((4, 1), 1, matrix) == (4, 0)

def test_print_path(capsys, get_matrix_1):
    matrix = get_matrix_1
    solution.print_path(matrix)
    captured = capsys.readouterr()
    expected_out = (
        "(4, 1)\n"
        "(4, 0)\n"
        "(3, 0)\n"
        "(2, 0)\n"
        "(2, 1)\n"
        "(2, 2)\n"
        "(2, 3)\n"
        "(1, 3)\n"
        "(0, 3)\n"
        "(0, 2)\n"
    )
    assert captured.out == expected_out

def test_alternate_path(get_matrix_1):
    matrix = get_matrix_1
    solution.alternate_path(matrix)
    expected = [
        [0, 0, 2, 1],
        [0, 0, 0, 2],
        [2, 1, 2, 1],
        [1, 0, 0, 0],
        [2, 1, 0, 0]
    ]
    assert matrix == expected

def test_count_path(get_matrix_1):
    matrix = get_matrix_1
    solution.count_path(matrix)
    expected = [
        [0, 0, 10, 9],
        [0, 0, 0, 8],
        [4, 5, 6, 7],
        [3, 0, 0, 0],
        [2, 1, 0, 0]
    ]
    assert matrix == expected

def test_mirror_horizontally(get_matrix_2):
    matrix = get_matrix_2
    solution.mirror_horizontally(matrix)
    expected = [
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0],
        [1, 1, 0, 1, 1]
    ]
    assert matrix == expected

def test_mirror_vertically(get_matrix_2):
    matrix = get_matrix_2
    solution.mirror_vertically(matrix)
    expected = [
        [0, 1, 0, 1, 1],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 0, 1, 1]
    ]
    assert matrix == expected
