import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_count_special():
    assert solution.count_special(["Bulb", "deed", "civic", "Noon"]) == 1
    assert solution.count_special(["ABBA", "aBba", "abca", "xyzzyx", "abcab", 'abcaca']) == 2
    assert solution.count_special(["abca", "aXba", "xyzzyx", "abcaXab"]) == 2
    assert solution.count_special(["hello", "world", "python", "java"]) == 0
    assert solution.count_special(["Anna", "Kayak", "Rotor", "Madam", "Level", 'Krok']) == 1
    assert solution.count_special(["axAA", "ByBB", "Czcc"]) == 3
