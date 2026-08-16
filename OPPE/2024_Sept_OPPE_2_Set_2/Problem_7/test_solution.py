import os
import subprocess
import sys

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

def test_reorder_lines_via_subprocess():
    tests = [
        ("2. Explicit is better than implicit.\n4. Complex is better than complicated.\n1. Beautiful is better than ugly.\n5. Flat is better than nested.\n3. Simple is better than complex.\n3,1,5,2,4\n",
         "1. Beautiful is better than ugly.\n2. Explicit is better than implicit.\n3. Simple is better than complex.\n4. Complex is better than complicated.\n5. Flat is better than nested.\n"),
        ("I love coding.\nProgramming is fun.\nSolving problems is rewarding.\n2,3,1\n",
         "Programming is fun.\nSolving problems is rewarding.\nI love coding.\n"),
        ("The quick brown fox jumps over the lazy dog.\nHello, world!\nPython is awesome.\nI am so confused.\n1,4,3,2\n",
         "The quick brown fox jumps over the lazy dog.\nI am so confused.\nPython is awesome.\nHello, world!\n")
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
