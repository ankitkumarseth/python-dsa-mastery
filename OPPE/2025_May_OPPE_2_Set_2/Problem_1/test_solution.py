import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_is_multiple_of_5_not_3():
    assert solution.is_multiple_of_5_not_3(10) is True
    assert solution.is_multiple_of_5_not_3(15) is False
    assert solution.is_multiple_of_5_not_3(-25) is True
    assert solution.is_multiple_of_5_not_3(9) is False
    assert solution.is_multiple_of_5_not_3(12) is False
    assert solution.is_multiple_of_5_not_3(0) is False  # 0 is a multiple of 3
    assert solution.is_multiple_of_5_not_3(5) is True
