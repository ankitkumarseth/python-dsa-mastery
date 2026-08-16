import os, importlib.util
SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_is_odd_indices_alpha_and_even_indices_digits():
    assert solution.is_odd_indices_alpha_and_even_indices_digits("a1b2c3") is False
    assert solution.is_odd_indices_alpha_and_even_indices_digits("1a2b3c") is True
    assert solution.is_odd_indices_alpha_and_even_indices_digits("3x4b6d") is True
    assert solution.is_odd_indices_alpha_and_even_indices_digits("123abc") is False
    # Edge case: empty string
    assert solution.is_odd_indices_alpha_and_even_indices_digits("") is True
    # Edge case: special characters
    assert solution.is_odd_indices_alpha_and_even_indices_digits("1@2b") is False

def test_has_a_in_second_half():
    assert solution.has_a_in_second_half("HelloWorld") is False
    assert solution.has_a_in_second_half("whenwhat") is True
    assert solution.has_a_in_second_half("whenWHAT") is True
    # Edge case: very short strings
    assert solution.has_a_in_second_half("aa") is True
    assert solution.has_a_in_second_half("bb") is False
    assert solution.has_a_in_second_half("") is False

def test_most_occuring_first_letter():
    passage1 = '''
This is a test sentence where I wanted
to let you know that the sentences are 
multi-line and words are separated by spaces.
The first letters may be of different case but you
should consider it as lowercase and return the lowercase
letter as the result. Also check the other test cases
where you can easily count the most occuring first letter.
    '''
    assert solution.most_occuring_first_letter(passage1) == 't'

    passage2 = '''
word1 Word2 word3 word4 text1 text2
text3 Text4 word5 text5 word6
python1 python2 Python3
    '''
    assert solution.most_occuring_first_letter(passage2) == 'w'

    passage3 = '''
aaaa bbbb cccc AAAA bbbb
CCCCCC DDDDD CCCCC CdcDC
abab cDcD
    '''
    assert solution.most_occuring_first_letter(passage3) == 'c'

def test_remove_edges():
    assert solution.remove_edges('abcdef') == 'cd'
    assert solution.remove_edges('abcdefghij') == 'cdefgh'
    assert solution.remove_edges('abcd') == ''
    # Edge cases: less than 4 characters
    assert solution.remove_edges('abc') == ''
    assert solution.remove_edges('a') == ''
    assert solution.remove_edges('') == ''
