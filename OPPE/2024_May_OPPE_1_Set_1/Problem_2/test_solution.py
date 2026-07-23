import os, pytest, importlib.util
SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_is_all_same_word_twice():
    strings = ["fast-fast", "slow-slow", "high-high", "low-low"]
    assert solution.is_all_same_word_twice(strings) is True
    strings2 = ["fast-slow", "slow-slow"]
    assert solution.is_all_same_word_twice(strings2) is False
    strings3 = ["fast-fast", "low-low-low"]
    assert solution.is_all_same_word_twice(strings3) is False
