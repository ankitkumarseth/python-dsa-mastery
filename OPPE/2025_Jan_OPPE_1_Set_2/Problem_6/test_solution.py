import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    employees = [
        {'name': 'Alice', 'department': 'HR', 'salary': 50000},
        {'name': 'Bob', 'department': 'Engineering', 'salary': 70000},
        {'name': 'Charlie', 'department': 'HR', 'salary': 45000},
        {'name': 'David', 'department': 'Engineering', 'salary': 60000},
        {'name': 'Eve', 'department': 'Marketing', 'salary': 55000},
    ]
    assert solution.employees_with_salary_above(employees, 50000) == ['Alice', 'Bob', 'David', 'Eve']
    assert solution.employees_with_salary_above(employees, 60000) == ['Bob', 'David']

def test_2():
    employees = [
        {'name': 'Alice', 'department': 'HR', 'salary': 50000},
        {'name': 'Bob', 'department': 'Engineering', 'salary': 70000},
        {'name': 'Charlie', 'department': 'HR', 'salary': 45000},
        {'name': 'David', 'department': 'Engineering', 'salary': 60000},
        {'name': 'Eve', 'department': 'Marketing', 'salary': 55000},
    ]
    assert solution.total_salary_in_department(employees, 'Engineering') == 130000
    assert solution.total_salary_in_department(employees, 'HR') == 95000

def test_3():
    assert solution.ceil_to_five_hundreds(24500) == 24500
    assert solution.ceil_to_five_hundreds(24600) == 25000
    assert solution.ceil_to_five_hundreds(24400) == 24500

def test_4():
    employees = [
        {'name': 'Alice', 'department': 'HR', 'salary': 50000},
        {'name': 'Bob', 'department': 'Engineering', 'salary': 70000},
        {'name': 'Charlie', 'department': 'HR', 'salary': 45000},
        {'name': 'David', 'department': 'Engineering', 'salary': 60000},
        {'name': 'Eve', 'department': 'Marketing', 'salary': 55000},
    ]
    assert solution.max_salary_after_increment_in_department(employees, 'HR', 10) == 55000
    assert solution.max_salary_after_increment_in_department(employees, 'Engineering', 7) == 75000
