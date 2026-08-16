import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_longest_common_prefix():
    assert solution.longest_common_prefix('flower flow flight') == 'fl'
    assert solution.longest_common_prefix('dog racecar car elephant') == ''
    assert solution.longest_common_prefix('apple application appreciate') == 'app'
    assert solution.longest_common_prefix('same same same') == 'same'
    assert solution.longest_common_prefix('a') == 'a'
