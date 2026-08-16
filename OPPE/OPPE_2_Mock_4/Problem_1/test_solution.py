import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_second_largest():
    assert solution.second_largest([1, 2, 3, 4, 5]) == 4
    assert solution.second_largest([3, 2, 1]) == 2

def test_arithmetic_operations():
    assert solution.arithmetic_operations((1, 2)) == (3, -1, 2, 0)
    assert solution.arithmetic_operations((10, 5)) == (15, 5, 50, 2)

def test_not_present_in_both():
    assert solution.not_present_in_both([1, 2, 3], [3, 4, 5]) == {1, 2, 4, 5}
    assert solution.not_present_in_both(['apple', 'ball', 'cat'], ['ball', 'cat', 'dog']) == {'apple', 'dog'}

def test_modify_string_1():
    assert solution.modify_string_1('abcde') == 'acedb'
    assert solution.modify_string_1('python') == 'ptonhy'

def test_create_count_dict():
    assert solution.create_count_dict(['a', 'b', 'c'], ['a', 'b', 'a', 'a', 'c', 'c', 'c']) == {'a': 3, 'b': 1, 'c': 3}

def test_average_of_numbers():
    assert solution.average_of_numbers([1, 2.5, 'a', 3, 'b']) == 2.17
    assert solution.average_of_numbers([32, 2, 12, 534, 4, 3]) == 97.83
