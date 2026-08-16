import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_process_employees():
    employee_list = [
        {'employee_id': 1, 'tasks_completed': 30, 'hours_worked': 40},
        {'employee_id': 2, 'tasks_completed': 60, 'hours_worked': 90},
        {'employee_id': 3, 'tasks_completed': 60, 'hours_worked': 100},
        {'employee_id': 4, 'tasks_completed': 50, 'hours_worked': 100},
        {'employee_id': 5, 'tasks_completed': 10, 'hours_worked': 30},
    ]

    assert solution.process_employees(employee_list, 'total_tasks_completed') == 210
    assert solution.process_employees(employee_list, 'most_efficient_employee') == 1
    assert solution.process_employees(employee_list, 'sort_by_hours_worked') == [3, 4, 2, 1, 5]
    assert solution.process_employees(employee_list, 'productive_team_members') == [1, 2, 3, 4]

    employee_list_2 = [
        {'employee_id': 1, 'tasks_completed': 60, 'hours_worked': 90},
        {'employee_id': 2, 'tasks_completed': 60, 'hours_worked': 100},
        {'employee_id': 3, 'tasks_completed': 60, 'hours_worked': 80},
        {'employee_id': 4, 'tasks_completed': 50, 'hours_worked': 100},
        {'employee_id': 5, 'tasks_completed': 10, 'hours_worked': 30},
    ]
    assert solution.process_employees(employee_list_2, 'most_efficient_employee') == 3

    employee_list_3 = [
        {'employee_id': 1, 'tasks_completed': 30, 'hours_worked': 40},
        {'employee_id': 2, 'tasks_completed': 20, 'hours_worked': 90},
        {'employee_id': 3, 'tasks_completed': 15, 'hours_worked': 100},
        {'employee_id': 4, 'tasks_completed': 50, 'hours_worked': 100},
        {'employee_id': 5, 'tasks_completed': 10, 'hours_worked': 30},
    ]
    assert solution.process_employees(employee_list_3, 'productive_team_members') == [1, 2, 4]
