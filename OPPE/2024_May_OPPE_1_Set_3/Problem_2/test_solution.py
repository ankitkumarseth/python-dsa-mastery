import os, importlib.util
SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_num_to_word():
    assert solution.num_to_word(123) == "one-two-three"
    assert solution.num_to_word(456) == "four-five-six"
