import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_best_performers():
    overs1 = [
        {'Bumrah': [1, 2, 'W', 0, 2, 'Wd', 0]},
        {'Shami': ['Nb[4]', 2, 1, 0, 'W', 'Wd', 'Wd', 4, 0]},
        {'Ashwin': [1, 4, 0, 3, 2, 1]}, 
        {'Shami': ['W', 2, 0, 0, 'Wd', 2, 6]},
        {'Bumrah': ['W', 'W', 1, 1, 0, 0]} 
    ]
    assert solution.best_performers(overs1) == [
        ('Bumrah', 3, 4.0),
        ('Shami', 2, 12.5),
        ('Ashwin', 0, 11.0)
    ]

    overs2 = [
        {"Shaheen Afridi": [4, 0, 2, 'W', 6, 'Nb[2]', 1]},
        {"Hasan Ali": [6, 4, 1, 'W', 0, 2]},
        {"Haris Rauf": [1, 4, 0, 6, 2, 'W']},
        {"Shaheen Afridi": ['W', 'Wd', 'Wd', 6, 1, 4, 0, 2]},
        {"Hasan Ali": [4, 6, 'W', 'Wd', 'Nb[6]', 0, 2, 1]},
        {"Haris Rauf": [2, 1, 6, 4, 0, 'W']},
        {"Shaheen Afridi": [2, 1, 'W', 'Nb[0]', 4, 6, 'W']},
        {"Hasan Ali": [1, 2, 'W', 6, 4, 0]},
        {"Haris Rauf": [6, 0, 4, 1, 2, 'W']}
    ]
    assert solution.best_performers(overs2) == [
        ('Shaheen Afridi', 4, 15.0),
        ('Haris Rauf', 3, 13.0),
        ('Hasan Ali', 3, 15.67)
    ]
