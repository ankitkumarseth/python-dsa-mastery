import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_absolute_time_difference():
    assert solution.absolute_time_difference('14:30', '06:45') == '07:45'
    assert solution.absolute_time_difference('06:45', '15:30') == '08:45'
    assert solution.absolute_time_difference('23:59', '00:00') == '23:59'
    assert solution.absolute_time_difference('23:58', '23:59') == '00:01'
    assert solution.absolute_time_difference('12:00', '12:00') == '00:00'
