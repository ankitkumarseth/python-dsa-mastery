import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_squares_of_odds():
    assert solution.squares_of_odds([1, 2, 3, 4, 5]) == [1, 9, 25]
    assert solution.squares_of_odds([2, 4, 6]) == []

def test_pair_elements():
    assert solution.pair_elements((1, 2, 3), ('a', 'b', 'c')) == ((1, 'a'), (2, 'b'), (3, 'c'))
    assert solution.pair_elements((4, 5), (6, 7)) == ((4, 6), (5, 7))

def test_modify_string_2():
    assert solution.modify_string_2(('hello', 'python')) == 'python, hello'
    assert solution.modify_string_2((1, 2)) == '2, 1'

def test_unique_vowels():
    assert solution.unique_vowels('aeiouAEIOU') == {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
    assert solution.unique_vowels("how's the josh!!!") == {'e', 'o'}

def test_invert_dictionary():
    assert solution.invert_dictionary({'a': 1, 'b': 2, 'c': 3}) == {1: 'a', 2: 'b', 3: 'c'}
    assert solution.invert_dictionary({1: 'a', 2: 'b', 3: 'c'}) == {'a': 1, 'b': 2, 'c': 3}

def test_factorial():
    assert solution.factorial(5) == 120
    assert solution.factorial(-5) == -120
