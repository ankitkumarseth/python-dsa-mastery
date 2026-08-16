import os
import subprocess
import sys

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

def test_vowel_case_via_subprocess():
    tests = [
        (
            "3\nThis is a sample text.\nit has many vowels.\nevery third one becomes uppercase.\n",
            "This is A sample tExt.\nit has mAny vowels.\nEvery third One becOmes uppErcase.\n"
        ),
        (
            "5\nThe quick brown fox jumps over the lazy dog.\nA simple and elegant exercise in typography.\n",
            "The quick brown fOx jumps over the lAzy dog.\na simple And elegant exErcise in typogrAphy.\n"
        ),
        (
            "2\nProgramming is the art of algorithm design\nand the craft of debugging.\n",
            "ProgrAmming Is the Art of AlgorIthm desIgn\nand thE craft Of debUgging.\n"
        ),
        (
            "1\nMake all vowels uppercase.\n",
            "MAkE All vOwEls UppErcAsE.\n"
        ),
        (
            "2\nHALF UPPER half lower\n",
            "HaLF UPPeR hAlf lowEr\n"
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
