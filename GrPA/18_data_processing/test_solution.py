import os
import importlib.util
import subprocess
import sys

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)


def test_row_index_with_most_number_of_zeros():
    matrix1 = [
        [1, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 1, 1]
    ]
    assert solution.row_index_with_most_number_of_zeros(matrix1) == 0

    matrix2 = [
        [1, 1, 1, 1],
        [0, 0, 1, 0],
        [1, 0, 0, 1],
        [0, 0, 0, 0]
    ]
    assert solution.row_index_with_most_number_of_zeros(matrix2) == 3

    matrix3 = [
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 1]
    ]
    assert solution.row_index_with_most_number_of_zeros(matrix3) == 1


def test_courses_sorted_by_enrollment():
    student_courses1 = {
        '101': ['Math', 'Science'],
        '102': ['Math'],
        '103': ['Science', 'Math'],
        '104': ['Math', 'History'],
        '105': ['English', 'History', 'Science']
    }
    assert solution.courses_sorted_by_enrollment(student_courses1) == ['Math', 'Science', 'History', 'English']

    student_courses2 = {
        '201': ['Biology', 'Chemistry'],
        '202': ['Chemistry', 'Biology'],
        '203': ['Physics', 'Chemistry'],
        '204': ['Biology', 'Physics'],
        '205': ['Chemistry']
    }
    assert solution.courses_sorted_by_enrollment(student_courses2) == ['Chemistry', 'Biology', 'Physics']


def test_antakshari_property_via_subprocess():
    """
    Tests Problem 3 (Antakshari) which expects inputs via sys.stdin and outputs via print()
    """
    input_data = "2\none,two,order,real,long,tight,tree,cool,lot,trouble\nant,tree,ear,rat,tower,retail\n"
    expected_output = "4\n6\n"

    # Run solution.py as a subprocess and pass standard input
    process = subprocess.Popen(
        [sys.executable, SOLUTION_FILE],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=input_data)

    # Note: If the user hasn't implemented it yet, stdout might be empty.
    # The test will fail until it's implemented.
    # We strip trailing whitespace to make comparison robust against extra newlines.
    assert stdout.strip() == expected_output.strip()


def test_num_to_word():
    assert solution.num_to_word(123) == "one-two-three"
    assert solution.num_to_word(456) == "four-five-six"
    # Edge cases
    assert solution.num_to_word(0) == "zero"
    assert solution.num_to_word(909) == "nine-zero-nine"
