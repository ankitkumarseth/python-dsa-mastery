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
    input_data = "9\nab__cd_ef__h_i_j\nk_lmn_op_q_r\ns__tuv___w\n"
    expected = "ab12cd3ef45h6i7j\nk8lmn9op_q_r\ns__tuv___w"
    assert run_test(input_data) == expected

def test_2():
    input_data = "5\nabc_def_ghi\njkl_mno_pqr\nstu_vwx_yz\n"
    expected = "abc1def2ghi\njkl3mno4pqr\nstu5vwx_yz"
    assert run_test(input_data) == expected

def test_3():
    input_data = "3\n_a_b_c_\n_d_e_\n"
    expected = "1a2b3c_\n_d_e_"
    assert run_test(input_data) == expected
