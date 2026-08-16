import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_digit_product():
    assert solution.digit_product(123) == 6
    assert solution.digit_product(101) == 0

def test_capitalize_first_and_last():
    assert solution.capitalize_first_and_last("hello world") == 'HellO WorlD'
    assert solution.capitalize_first_and_last("python programming") == 'PythoN ProgramminG'

def test_kth_longest_word():
    assert solution.kth_longest_word(['apple', 'banana', 'blueberry', 'date'], 2) == 'banana'
    assert solution.kth_longest_word(['elephant', 'dog', 'cats', 'hippopotamus'], 1) == 'hippopotamus'
    assert solution.kth_longest_word(['a', 'abc', 'abcd', 'ab'], 3) == 'ab'

def test_unflatten():
    assert solution.unflatten((1, 2, 3, 4, 5, 6), 2, 3) == ((1, 2, 3), (4, 5, 6))
    assert solution.unflatten((1, 2, 3, 4), 2, 2) == ((1, 2), (3, 4))

def test_is_heterogram():
    assert solution.is_heterogram('The big dwarf only jumps') is True
    assert solution.is_heterogram('Blue bat') is False
    assert solution.is_heterogram('Hello World') is False

def test_filter_keys_by_value():
    d1 = {'a': 1, 'b': 5, 'c': 3}
    solution.filter_keys_by_value(d1, 3)
    assert d1 == {'b': 5}

    d2 = {1: 10, 2: 20, 3: 5, 4: 30}
    solution.filter_keys_by_value(d2, 15)
    assert d2 == {2: 20, 4: 30}
