import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_sort_tuples_by_second_then_third():
    assert solution.sort_tuples_by_second_then_third([(0,2,0),(1,2,1),(-6,2,1),(0,2,1),(-9,1,0),(5,2,-1)]) == [(-9, 1, 0), (5, 2, -1), (0, 2, 0), (-6, 2, 1), (0, 2, 1), (1, 2, 1)]
    assert solution.sort_tuples_by_second_then_third([(4,-5,4),(-9,5,4),(-6,2,1),(0,-2,-1),(5,5,4),(5,2,-1)]) == [(4, -5, 4), (0, -2, -1), (5, 2, -1), (-6, 2, 1), (-9, 5, 4), (5, 5, 4)]
