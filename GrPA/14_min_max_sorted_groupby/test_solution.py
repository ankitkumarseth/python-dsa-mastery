import os
import ast
import inspect
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def has_if_or_loops(func):
    source = inspect.getsource(func)
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, (ast.If, ast.For, ast.While, ast.AsyncFor, ast.AsyncFunctionDef)):
            return True
    return False

def has_comprehensions(func):
    source = inspect.getsource(func)
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
            return True
    return False

@pytest.fixture


def dummy_students():
    return [
        {"rollno": 1, "city": "Chennai", "marks": {"CT": 80, "Math-1": 90, "Stats-1": 85}},
        {"rollno": 2, "city": "Mumbai", "marks": {"CT": 90, "Math-1": 80, "Stats-1": 90}},
        {"rollno": 3, "city": "Mumbai", "marks": {"CT": 85, "Math-1": 85, "Stats-1": 85}},
        {"rollno": 4, "city": "Delhi", "marks": {"CT": 70, "Math-1": 70, "Stats-1": 70}}
    ]

def test_groupby():
    fruits = ["Apple", "Banana", "Avocado", "Amla", "Black berry", "Blue berry"]
    expected = {
        "A": ["Apple", "Avocado", "Amla"],
        "B": ["Banana", "Black berry", "Blue berry"]
    }
    assert solution.groupby(fruits, lambda x: x[0]) == expected

def test_apply_to_groups():
    groups = {
      "A": ["Apple", "Avocado"],
      "B": ["Banana", "Black berry", "Blue berry"]
    }
    assert solution.apply_to_groups(groups, len) == {"A": 2, "B": 3}

def test_no_loops_or_comps_enforced():
    funcs_to_check = [
        solution.min_course_marks,
        solution.max_course_marks,
        solution.rollno_of_max_marks,
        solution.sort_rollno_by_marks,
        solution.count_students_by_cities,
        solution.city_with_max_no_of_students,
        solution.group_rollnos_by_cities,
        solution.city_with_max_avg_course_mark
    ]
    for func in funcs_to_check:
        assert not has_if_or_loops(func), f"{func.__name__} has loops/ifs!"
        assert not has_comprehensions(func), f"{func.__name__} has comprehensions!"

def test_student_data_operations(dummy_students):
    assert solution.min_course_marks(dummy_students, "CT") == 70
    assert solution.max_course_marks(dummy_students, "Math-1") == 90
    assert solution.rollno_of_max_marks(dummy_students, "Stats-1") == 2

    # Sort order checking: ascending by marks
    assert solution.sort_rollno_by_marks(dummy_students, "CT", "Math-1", "Stats-1") == [4, 1, 3, 2]

    assert solution.count_students_by_cities(dummy_students) == {"Chennai": 1, "Mumbai": 2, "Delhi": 1}
    assert solution.city_with_max_no_of_students(dummy_students) == "Mumbai"

    assert solution.group_rollnos_by_cities(dummy_students) == {
        "Chennai": [1],
        "Mumbai": [2, 3],
        "Delhi": [4]
    }

    # Mumbai avg CT = (90+85)/2 = 87.5
    # Chennai avg CT = 80
    # Delhi avg CT = 70
    assert solution.city_with_max_avg_course_mark(dummy_students, "CT") == "Mumbai"
