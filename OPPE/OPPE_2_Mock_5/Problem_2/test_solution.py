import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_rotate_list():
    assert solution.rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert solution.rotate_list(['a', 'b', 'c', 'd', 'e'], 3) == ['c', 'd', 'e', 'a', 'b']
