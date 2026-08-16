import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_n_happy_numbers():
    assert solution.n_happy_numbers([1, 65, 28, 23, 60, 31]) == 4
    assert solution.n_happy_numbers([96, 74, 79, 48, 81, 31, 29, 63]) == 2
    assert solution.n_happy_numbers([19, 2, 7, 4, 10, 28]) == 4
