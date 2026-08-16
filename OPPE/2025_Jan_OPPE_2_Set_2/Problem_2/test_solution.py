import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_shuffle_sentence():
    assert solution.shuffle_sentence('apple banana orange', (0, 2, 1)) == 'apple orange banana'
    assert solution.shuffle_sentence('cat dog mouse', (2, 1, 0)) == 'mouse dog cat'
    assert solution.shuffle_sentence('red yellow green', (1, 0, 2)) == 'yellow red green'
