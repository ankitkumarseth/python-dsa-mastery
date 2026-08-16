import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_valid_substring():
    assert solution.valid_substring('applebanana', ['apple', 'banana', 'pine', 'melon']) is True
    assert solution.valid_substring('pineapple', ['apple', 'banana', 'mango']) is False
    assert solution.valid_substring('helloworld', ['hello', 'world', 'good', 'bye']) is True
    assert solution.valid_substring('hellogoodbye', ['hello', 'world', 'good', 'bye']) is False
