import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_words_with_consecutive_letters():
    words1 = ['hello', 'apple', 'ball', 'test', 'cat']
    assert solution.words_with_consecutive_letters(words1) == ['hello', 'apple', 'ball']

    words2 = ['sky', 'fly', 'run', 'jump']
    assert solution.words_with_consecutive_letters(words2) == []

    words3 = ['mississippi', 'apple', 'call', 'keep']
    assert solution.words_with_consecutive_letters(words3) == ['mississippi', 'apple', 'call', 'keep']
    
    words4 = ['aPple', 'bAll']
    assert solution.words_with_consecutive_letters(words4) == ['aPple', 'bAll']
