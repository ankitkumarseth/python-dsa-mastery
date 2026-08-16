import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_most_frequent_element():
    assert solution.most_frequent_element([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4
    assert solution.most_frequent_element([15, 15, 22, 41, 55]) == 15
    # If multiple with same frequency, return the largest
    assert solution.most_frequent_element([1, 1, 5, 5, 3]) == 5
