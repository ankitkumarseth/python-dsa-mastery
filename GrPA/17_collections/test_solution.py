import os, importlib.util
SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_reverse_first_half():
    assert solution.reverse_first_half((10, 20, 30, 40, 50, 60)) == (30, 20, 10, 40, 50, 60)
    assert solution.reverse_first_half(('a', 'b', 'c', 'd')) == ('b', 'a', 'c', 'd')
    assert solution.reverse_first_half((1, 2)) == (1, 2)
    # Edge case: empty tuple
    assert solution.reverse_first_half(()) == ()

def test_delete_first_three():
    l1 = [10, 20, 30, 40, 50]
    solution.delete_first_three(l1)
    assert l1 == [40, 50]

    l2 = [1, 2, 3, 4, 5, 6, 7]
    solution.delete_first_three(l2)
    assert l2 == [4, 5, 6, 7]

    l3 = [1, 2]
    solution.delete_first_three(l3)
    assert l3 == []

    # Edge cases
    l4 = [1, 2, 3]
    solution.delete_first_three(l4)
    assert l4 == []

    l5 = []
    solution.delete_first_three(l5)
    assert l5 == []

def test_number_of_unique_common_digits():
    assert solution.number_of_unique_common_digits(12345, 54321) == 5
    assert solution.number_of_unique_common_digits(287498, 295424) == 3
    assert solution.number_of_unique_common_digits(67890, 9876) == 4
    # Edge case: no common digits
    assert solution.number_of_unique_common_digits(123, 456) == 0

def test_final_position():
    assert solution.final_position((1, 1), (2, 2), 3) == (7, 7)
    assert solution.final_position((1, 2), (2, 1), 3) == (7, 5)
    assert solution.final_position((1, 1), (1, 1), 2) == (3, 3)
    # Edge case: zero velocity
    assert solution.final_position((5, 5), (0, 0), 10) == (5, 5)
    # Edge case: zero time
    assert solution.final_position((4, 4), (10, 10), 0) == (4, 4)
