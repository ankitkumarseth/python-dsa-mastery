import os
import subprocess
import sys

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

def test_fill_blanks_via_subprocess():
    tests = [
        (
            "11\na_bc__d___e\nf_g__h__i__j\nk___l_m__n\n",
            "a1bc23d456e\nf7g89h1011i__j\nk___l_m__n\n"
        ),
        (
            "9\nab__cd_ef__h_i_j\nk_lmn_op_q_r\ns__tuv___w\n",
            "ab12cd3ef45h6i7j\nk8lmn9op_q_r\ns__tuv___w\n"
        ),
        (
            "5\nabc_def_ghi\njkl_mno_pqr\nstu_vwx_yz\n",
            "abc1def2ghi\njkl3mno4pqr\nstu5vwx_yz\n"
        ),
        (
            "3\n_a_b_c_\n_d_e_\n",
            "1a2b3c_\n_d_e_\n"
        )
    ]
    
    input_file_path = os.path.join(os.path.dirname(__file__), 'test_input.txt')

    for input_data, expected_output in tests:
        # Write the specific test case to test_input.txt
        with open(input_file_path, 'w') as f:
            f.write(input_data)
            
        # We run the solution.py file which should read test_input.txt and print
        process = subprocess.Popen(
            [sys.executable, SOLUTION_FILE],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=os.path.dirname(__file__) # Run in the same directory so test_input.txt is found
        )
        stdout, stderr = process.communicate()
        
        # We strip trailing whitespace to make comparison robust
        assert stdout.strip() == expected_output.strip()
