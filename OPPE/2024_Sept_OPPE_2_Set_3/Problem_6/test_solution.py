import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    points = {
        (2, 5), (-2, 6), (-2, 7), (-1, 3),
        (-3, -4), (4, -6), (0, 7)
    }
    output = [
        (0, 7), (-1, 3), (2, 5), (-2, 7),
        (-2, 6), (-3, -4), (4, -6)
    ]
    assert solution.process_points(points, "sort_close_to_y_axis") == output

def test_2():
    points = {
        (2, 5), (-1, 3), (1, 3), (-3, -4),
        (4, -6), (5, -1)
    }
    assert solution.process_points(points, "closest_point_to_origin") == (1, 3)

def test_3():
    points = {(2, 5), (-1, 3), (-3, -4), (4, -6), (5, -1)}
    output = {
        1: {(2, 5)}, 2: {(-1, 3)}, 
        3: {(-3, -4)}, 4: {(4, -6), (5, -1)}
    }
    assert solution.process_points(points, "group_by_quadrant") == output
