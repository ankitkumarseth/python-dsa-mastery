import os, importlib.util
SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_courses_sorted():
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
