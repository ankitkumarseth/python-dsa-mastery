import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_extract_border_elements():
    assert solution.extract_border_elements([1, 2, 3, 4]) == [1, 4]
    assert solution.extract_border_elements([5]) == [5]
    assert solution.extract_border_elements([]) == []
    assert solution.extract_border_elements([10, 20, 30, 40, 50]) == [10, 50]
