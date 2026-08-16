import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_remove_second_and_second_last():
    assert solution.remove_second_and_second_last("abcdef") == "acdf"
    assert solution.remove_second_and_second_last("abcd") == "ad"
    assert solution.remove_second_and_second_last("alpha") == "apa"
    assert solution.remove_second_and_second_last("hello") == "hlo"
