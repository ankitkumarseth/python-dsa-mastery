import os
import subprocess
import sys

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

def test_hand_cricket_via_subprocess():
    """
    Tests Problem 5 (Hand Cricket) which expects inputs via sys.stdin and outputs via print()
    """
    tests = [
        (
            "1 4\n2 3\n6 2\n5 1\n0 2\n3 3\n",
            "6 16\n"
        ),
        (
            "1 4\n5 3\n0 3\n5 1\n5 4\n",
            "5 14\n"
        ),
        (
            "1 0\n0 5\n2 4\n4 4\n",
            "4 8\n"
        ),
        (
            "2 0\n3 1\n6 5\n2 0\n0 4\n5 3\n4 5\n1 4\n0 5\n2 5\n2 6\n",
            "11 34\n"
        ),
        (
            "6 0\n3 1\n2 3\n6 2\n5 3\n1 0\n3 5\n0 2\n1 1\n",
            "9 28\n"
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
        
        # Strip trailing whitespace to make comparison robust against extra newlines
        assert stdout.strip() == expected_output.strip()
