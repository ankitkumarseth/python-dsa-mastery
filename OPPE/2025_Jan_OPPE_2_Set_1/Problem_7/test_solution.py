import os
import subprocess
import sys

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

def test_string_rearrangement_via_subprocess():
    tests = [
        ("hello,2,1,3,5,4\n", "ehlol\n"),
        ("abcdef,3,2,1,6,5,4\n", "cbafed\n"),
        ("xyz,3,1,2\n", "zxy\n")
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
