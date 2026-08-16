import os
import subprocess
import sys

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

def test_total_size_of_images_via_subprocess():
    tests = [
        (
            "2000,file1.jpg\n890,file2.txt\n30500,file3.JPEG\n12000,file4.png\n40000,file5.gif\n490,file6.docx\n",
            "84500\n"
        ),
        (
            "123,file1.jpg\n456,file2.txt\n789,file3.42.jpeg\n1011,A.B.something.PNG\n1213,file5.gif\n456,file6.xls\n2453,file7.csv\n23256,file7.mov\n",
            "3136\n"
        ),
        (
            "100,file1.jpg\n200,file2.txt\n300,file3.jpeg\n400,file4.png\n500,file5.pdf\n",
            "800\n"
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
