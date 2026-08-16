import os
import subprocess
import sys

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

def test_make_word_via_subprocess():
    tests = [
        (
            "3 a\n5\napple\nant\nbanana\nanchor\ncat\n",
            "etr\n"
        ),
        (
            "5 B\n7\nBanana\nberry\nBubble\nbubble\ntin\nBoat\nBison\n",
            "aen\n"
        ),
        (
            "2 x\n4\nxylophone\nXenon\nx-ray\nextra\n",
            "ey\n"
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
        
        # Check against expected, dealing gracefully with empty output vs empty line
        if not expected_output.strip():
            assert not stdout.strip()
        else:
            assert stdout.strip() == expected_output.strip()
