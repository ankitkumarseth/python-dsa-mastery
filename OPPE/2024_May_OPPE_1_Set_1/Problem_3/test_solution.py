import os, pytest, importlib.util
SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_most_occuring_first_letter():
    passage = '''
    word1 Word2 word3 word4 text1 text2
    text3 Text4 word5 text5 word6
    python1 python2 Python3
    '''
    assert solution.most_occuring_first_letter(passage) == 'w'

    passage2 = '''
    aaaa bbbb cccc AAAA bbbb
    CCCCCC DDDDD CCCCC CdcDC
    abab cDcD
    '''
    assert solution.most_occuring_first_letter(passage2) == 'c'
