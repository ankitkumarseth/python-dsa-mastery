import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_same_sign():
    assert solution.same_sign(10, 20) is True
    assert solution.same_sign(-5, -15) is True
    assert solution.same_sign(0, 0) is True
    assert solution.same_sign(10, -20) is False
    assert solution.same_sign(0, 10) is False
    assert solution.same_sign(-10, 0) is False
