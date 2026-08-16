import os
import subprocess
import sys

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

def test_simple_stemmer_via_subprocess():
    tests = [
        (
            "running faster stronger\norganization management\nhappiness joyfulness sadness\n",
            "runn fast strong\norganiz manage\nhappi joyful sad\n"
        ),
        (
            "beautiful wonderful amazing\ncommunication information education\nentertainment enjoyment relaxation\n",
            "beauti wonder amaz\ncommunic inform educ\nentertain enjoy relax\n"
        ),
        (
            "productivity efficiency effectiveness\nmotivation inspiration imagination\ncreation innovation realization\n",
            "productiv efficiency effective\nmotiv inspir imagin\ncre innov realiz\n"
        ),
        (
            "exploration investigation consideration\ncelebration conversation education\n",
            "explor investig consider\ncelebr convers educ\n"
        ),
        (
            "hello world this is python\nprogramming language is fun\nto learn and practice\n",
            "hello world this is python\nprogramm langu is fun\nto learn and practice\n"
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
