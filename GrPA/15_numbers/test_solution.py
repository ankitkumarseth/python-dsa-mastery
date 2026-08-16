import os, importlib.util
SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_seconds_to_minute_seconds():
    assert solution.seconds_to_minute_seconds(125) == (2, 5)
    assert solution.seconds_to_minute_seconds(3600) == (60, 0)
    assert solution.seconds_to_minute_seconds(75) == (1, 15)
    assert solution.seconds_to_minute_seconds(0) == (0, 0)

def test_create_indexed_dict():
    names1 = ["Alice", "Bob", "Charlie", "David"]
    expected1 = {0: "Alice", 1: "Bob", 2: "Charlie", 3: "David"}
    assert solution.create_indexed_dict(names1) == expected1

    names2 = ["Apple", "Banana", "Cherry", "Date"]
    expected2 = {0: "Apple", 1: "Banana", 2: "Cherry", 3: "Date"}
    assert solution.create_indexed_dict(names2) == expected2

def test_manhattan_distance_via_b():
    assert solution.manhattan_distance_via_b((1, 2), (3, 4), (6, 7)) == 10
    assert solution.manhattan_distance_via_b((0, 0), (2, 2), (3, 3)) == 6
    assert solution.manhattan_distance_via_b((-1, -1), (1, 1), (2, 2)) == 6

def test_is_right_triangle_with_even_sides():
    assert solution.is_right_triangle_with_even_sides(3, 3, 5) is False
    assert solution.is_right_triangle_with_even_sides(6, 8, 10) is True
    assert solution.is_right_triangle_with_even_sides(3, 4, 5) is False
    assert solution.is_right_triangle_with_even_sides(4, 6, 8) is False
