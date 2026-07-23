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
    input_data = "2. Explicit is better than implicit.\n4. Complex is better than complicated.\n1. Beautiful is better than ugly.\n5. Flat is better than nested.\n3. Simple is better than complex.\n3,1,5,2,4\n"
    expected = "1. Beautiful is better than ugly.\n2. Explicit is better than implicit.\n3. Simple is better than complex.\n4. Complex is better than complicated.\n5. Flat is better than nested."
    assert run_test(input_data) == expected

def test_2():
    input_data = "I love coding.\nProgramming is fun.\nSolving problems is rewarding.\n2,3,1\n"
    expected = "Programming is fun.\nSolving problems is rewarding.\nI love coding."
    assert run_test(input_data) == expected

def test_3():
    input_data = "The quick brown fox jumps over the lazy dog.\nHello, world!\nPython is awesome.\nI am so confused.\n1,4,3,2\n"
    expected = "The quick brown fox jumps over the lazy dog.\nI am so confused.\nPython is awesome.\nHello, world!"
    assert run_test(input_data) == expected
