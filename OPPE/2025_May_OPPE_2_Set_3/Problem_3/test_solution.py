import os
import importlib.util
import copy

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_add_average_key_diff():
    d = {1: 5, 3: 9}
    solution.add_average_key_diff(d, 1, 3)
    assert d == {1: 5, 2: 4, 3: 9}

    d2 = {10: 100, 20: 40, 30: 70}
    solution.add_average_key_diff(d2, 10, 30)
    assert d2 == {10: 100, 20: 30, 30: 70}

    d3 = {5: 3, 7: -3}
    solution.add_average_key_diff(d3, 5, 7)
    assert d3 == {5: 3, 6: 6, 7: -3}
