import os
import subprocess
import sys

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

def test_markdown_totals_via_subprocess():
    tests = [
        (
            "| Score |\n|------|\n| 10 |\n| 15 |\n| 20 |\n",
            "Score: 45\n"
        ),
        (
            "| A | B | C |\n|---|---|---|\n| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n",
            "A: 12\nB: 15\nC: 18\n"
        ),
        (
            "| Qty | Price |\n|-----|-------|\n| -5 | 1 |\n| 10 | 0 |\n| 0 | -2 |\n",
            "Qty: 5\nPrice: -1\n"
        ),
        (
            "| X |\n|---|\n| 100 |\n| -50 |\n| 25 |\n",
            "X: 75\n"
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
