import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_is_palindrome():
    assert solution.is_palindrome("A man, a plan, a canal, Panama!") is True
    assert solution.is_palindrome("racecar") is True
    assert solution.is_palindrome("Hello") is False
    assert solution.is_palindrome("Was it a car or a cat I saw?") is True
    assert solution.is_palindrome("10/02/2001") is True
    assert solution.is_palindrome("01/02/2001") is False
    # Edge Cases
    assert solution.is_palindrome("") is True
    assert solution.is_palindrome(".,!?") is True
