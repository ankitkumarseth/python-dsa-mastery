import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_most_frequent_alpha_character():
    # Test case 1
    input1 = """5
this is a line
this is second line
this line contains numbers like 1 2 3 4 5 
string can be special characters like @ # $ % ^
This is last line
"""
    file1 = os.path.join(os.path.dirname(__file__), 'test_input_1.txt')
    with open(file1, 'w') as f:
        f.write(input1)
    
    assert solution.most_frequent_alpha_character(file1) == ['i']

    # Test case 2
    input2 = """4
Lorem ipsum dolor sit amet consectetur adipisicing elit.
Natus quas quod excepturi eum veritatis enim molestiae nihil nulla.
Ab, doloribus facilis? Mollitia, rerum officia.
Ea illo deserunt soluta adipisci nemo.
"""
    file2 = os.path.join(os.path.dirname(__file__), 'test_input_2.txt')
    with open(file2, 'w') as f:
        f.write(input2)

    assert solution.most_frequent_alpha_character(file2) == ['i']
