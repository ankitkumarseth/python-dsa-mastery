import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_starts_with_greeting():
    assert solution.starts_with_greeting("Hello there") is True
    assert solution.starts_with_greeting("Hi friend") is True
    assert solution.starts_with_greeting("Hithere") is False
    assert solution.starts_with_greeting("Welcome") is False
    assert solution.starts_with_greeting("Hello World") is True
    assert solution.starts_with_greeting("HelloWorld") is False
    assert solution.starts_with_greeting("Hi ") is True
    assert solution.starts_with_greeting("Hello ") is True
