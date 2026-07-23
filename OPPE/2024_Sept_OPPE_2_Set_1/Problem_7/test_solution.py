import os
import sys
import pytest
import tempfile
from io import StringIO

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def run_test(input_data):
    # Write input to a temporary file
    with tempfile.NamedTemporaryFile('w', delete=False) as f:
        f.write(input_data)
        temp_file_name = f.name
        
    old_argv = sys.argv
    old_stdout = sys.stdout
    sys.argv = ['solution.py', temp_file_name]
    sys.stdout = StringIO()
    
    try:
        solution.solve()
        return sys.stdout.getvalue().strip()
    finally:
        sys.argv = old_argv
        sys.stdout = old_stdout
        os.remove(temp_file_name)

def test_1():
    input_data = "hello\n"
    expected = "hubelldubo"
    assert run_test(input_data) == expected

def test_2():
    input_data = "python programming is good\npython is the best\n"
    expected = "pythubon prdubogrubammdubing ubis gduboubod\npythdubon ubis thdube bubest"
    assert run_test(input_data) == expected

def test_3():
    input_data = "amazing things happen\nevery now and then\n"
    expected = "ubamdubazubing thdubings hubappduben\nubevdubery nubow duband thuben"
    assert run_test(input_data) == expected
