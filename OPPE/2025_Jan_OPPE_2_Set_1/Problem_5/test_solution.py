import os
import subprocess
import sys

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

def test_thresholding_via_subprocess():
    """
    Tests Problem 5 (Thresholding) which expects inputs via sys.stdin and outputs via print()
    """
    tests = [
        (
            "3 100\n150 80 200\n90 250 60\n99 120 45\n",
            "@ * @\n* @ *\n* @ *\n"
        ),
        (
            "2 50\n10 51\n100 40\n",
            "* @\n@ *\n"
        ),
        (
            "4 150\n160 15 140 160\n120 255 240 100\n80 178 151 40\n183 20 10 166\n",
            "@ * * @\n* @ @ *\n* @ @ *\n@ * * @\n"
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
