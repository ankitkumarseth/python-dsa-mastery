import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_polygon_functions():
    points1 = [(0, 0), (3, 1), (5, 3), (3, 4), (1, 3)]
    assert round(solution.perimeter(points1)) == 14
    assert solution.bounding_box(points1) == ((0, 0), (5, 4))
    assert round(solution.area(points1)) == 10
    assert solution.is_convex(points1) is True

    points2 = [(2, 1), (5, 2), (2, 3), (4, 5), (0, 4)]
    assert round(solution.perimeter(points2)) == 17
    assert solution.bounding_box(points2) == ((0, 1), (5, 5))
    assert round(solution.area(points2)) == 8
    assert solution.is_convex(points2) is False

    points3 = [(5, 3), (3, 4), (1, 3),(0, 0), (3, 1)]
    assert solution.is_convex(points3) is True
    
    points4 = [(4, 5), (0, 4), (2, 1), (5, 2), (2, 3)]
    assert solution.is_convex(points4) is False
    
    points5 = [(2, 3), (4, 5), (0, 4), (2, 1), (5, 2)]
    assert solution.is_convex(points5) is False
