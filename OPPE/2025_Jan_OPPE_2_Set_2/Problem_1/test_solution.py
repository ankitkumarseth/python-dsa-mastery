import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_extract_middle_elements():
    assert solution.extract_middle_elements([7, 8, 9, 10, 11, 12, 13]) == [10]
    assert solution.extract_middle_elements([3, 6, 9, 12, 15, 18]) == [9, 12]
    assert solution.extract_middle_elements([-10, -5, 0, 5]) == [-5, 0]
    # Edge Cases
    assert solution.extract_middle_elements([1]) == [1]
    assert solution.extract_middle_elements([1, 2]) == [1, 2]
    assert solution.extract_middle_elements([]) == []
