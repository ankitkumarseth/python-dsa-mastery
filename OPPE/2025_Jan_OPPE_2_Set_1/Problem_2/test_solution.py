import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_starts_and_ends_with_same_vowel():
    assert solution.starts_and_ends_with_same_vowel("Atta") is True
    assert solution.starts_and_ends_with_same_vowel("atta") is True
    assert solution.starts_and_ends_with_same_vowel("Tart") is False
    assert solution.starts_and_ends_with_same_vowel("TART") is False
    assert solution.starts_and_ends_with_same_vowel("Lioness") is False
    assert solution.starts_and_ends_with_same_vowel("Atrocity") is False
    assert solution.starts_and_ends_with_same_vowel("Achoo") is False
    # Edge Cases
    assert solution.starts_and_ends_with_same_vowel("A") is True
    assert solution.starts_and_ends_with_same_vowel("E") is True
    assert solution.starts_and_ends_with_same_vowel("Z") is False
    assert solution.starts_and_ends_with_same_vowel("") is False
