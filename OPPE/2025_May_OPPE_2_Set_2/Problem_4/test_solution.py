import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_reversed_squares():
    assert solution.reversed_squares([1, 2, 3, 4, 5]) == [25, 16, 9, 4, 1]
    assert solution.reversed_squares([10, 2]) == [4, 100]
    assert solution.reversed_squares([]) == []
    assert solution.reversed_squares([-2, 5]) == [25, 4]
    assert solution.reversed_squares([0]) == [0]
