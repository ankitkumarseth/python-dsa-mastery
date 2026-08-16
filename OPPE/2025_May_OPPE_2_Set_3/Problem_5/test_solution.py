import os
import subprocess
import sys

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

def test_remainder_grouping_via_subprocess():
    tests = [
        (
            "1,2,3,4,5,6\n3\n",
            "0 - 3,6\n1 - 1,4\n2 - 2,5\n"
        ),
        (
            "45,53,10,21,33\n5\n",
            "0 - 10,45\n1 - 21\n3 - 33,53\n"
        ),
        (
            "7,9,11,13,25,27,29\n7\n",
            "0 - 7\n1 - 29\n2 - 9\n4 - 11,25\n6 - 13,27\n"
        )
    ]

    for input_data, expected_output in tests:
        process = subprocess.Popen(
            [sys.executable, SOLUTION_FILE],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=input_data)
        
        assert stdout.strip() == expected_output.strip()
