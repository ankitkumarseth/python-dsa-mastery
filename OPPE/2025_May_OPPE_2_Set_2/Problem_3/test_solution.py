import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_combine_edges():
    assert solution.combine_edges('HelloWorld') == 'Held'
    assert solution.combine_edges('Python') == 'Pyon'
    assert solution.combine_edges('Hi') == ''
    assert solution.combine_edges('Programming') == 'Prng'
    assert solution.combine_edges('abcd') == 'abcd'
    assert solution.combine_edges('abc') == ''
    assert solution.combine_edges('') == ''
