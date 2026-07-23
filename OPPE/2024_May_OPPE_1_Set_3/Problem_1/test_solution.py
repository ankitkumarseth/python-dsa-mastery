import os, importlib.util
SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_square_and_clip():
    assert solution.square_and_clip(9,80) == 80
    assert solution.square_and_clip(9,100) == 81
    assert solution.square_and_clip(5,20) == 20
    assert solution.square_and_clip(5,25) == 25
    assert solution.square_and_clip(5,30) == 25

def test_lowercase_uppercase():
    assert solution.lowercase_first_half_and_uppercase_second_half("AbCdEfGh") == "abcdEFGH"
    assert solution.lowercase_first_half_and_uppercase_second_half("HELLOworld") == "helloWORLD"

def test_add_middle():
    l1 = [1, 2, 3, 4, 5]
    solution.add_the_middle_element_to_both_ends(l1)
    assert l1 == [3, 1, 2, 3, 4, 5, 3]

    l2 = [7, 8, 9, 10, 11]
    solution.add_the_middle_element_to_both_ends(l2)
    assert l2 == [9, 7, 8, 9, 10, 11, 9]

def test_unique_digits():
    assert solution.number_of_unique_common_digits(12345, 54321) == 5
    assert solution.number_of_unique_common_digits(287498, 295424) == 3
    assert solution.number_of_unique_common_digits(67890, 9876) == 4

def test_manhattan():
    assert solution.manhattan_distance_via_b((1, 2), (3, 4), (6, 7)) == 10
    assert solution.manhattan_distance_via_b((0, 0), (2, 2), (3, 3)) == 6
    assert solution.manhattan_distance_via_b((-1, -1), (1, 1), (2, 2)) == 6

def test_indexed_dict():
    names = ["Alice", "Bob", "Charlie", "David"]
    expected = {0: "Alice", 1: "Bob", 2: "Charlie", 3: "David"}
    assert solution.create_indexed_dict(names) == expected
