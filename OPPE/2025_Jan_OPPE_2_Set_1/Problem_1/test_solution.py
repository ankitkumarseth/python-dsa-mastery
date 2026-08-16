import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_is_multiple():
    assert solution.is_multiple(15, 3) is True
    assert solution.is_multiple(7, 21) is True
    assert solution.is_multiple(12, 5) is False
    assert solution.is_multiple(9, 27) is True
    # Edge Cases
    assert solution.is_multiple(10, 10) is True
    assert solution.is_multiple(0, 5) is True
