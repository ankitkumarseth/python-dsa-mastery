import os
import subprocess
import sys

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

def test_abbreviate_initials_via_subprocess():
    """
    Tests Problem 5 (Abbreviate Initials) which expects inputs via sys.stdin and outputs via print()
    """
    tests = [
        (
            "4\nJohn Doe\nAlice Johnson\nBob Alan Rickman\nAlbus Percival Wulfric Brian Dumbledore\n",
            "Doe, J.\nDumbledore, A.P.W.B.\nJohnson, A.\nRickman, B.A.\n"
        ),
        (
            "2\nZara Olsen\nAlex Trevor\n",
            "Olsen, Z.\nTrevor, A.\n"
        ),
        (
            "1\nChris Pratt\n",
            "Pratt, C.\n"
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
