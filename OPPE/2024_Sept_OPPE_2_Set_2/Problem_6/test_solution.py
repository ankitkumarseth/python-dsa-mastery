import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    logs = [
        {"name": "Alice", "duration": 300},
        {"name": "Bob", "duration": 200},
        {"name": "Alice", "duration": 100},
        {"name": "Bob", "duration": 400}
    ]
    assert solution.process_call_logs(logs, "get_call_counts") == {"Alice": 2, "Bob": 2}

def test_2():
    logs = [
        {"name": "Alice", "duration": 300},
        {"name": "Bob", "duration": 200},
        {"name": "Alice", "duration": 100},
        {"name": "Bob", "duration": 400}
    ]
    assert solution.process_call_logs(logs, "get_total_call_durations") == {"Alice": 400, "Bob": 600}

def test_3():
    logs = [
        {"name": "Alice", "duration": 300},
        {"name": "Bob", "duration": 200},
        {"name": "Alice", "duration": 100},
        {"name": "Bob", "duration": 400},
        {"name": "Charlie", "duration": 400}
    ]
    assert solution.process_call_logs(logs, "most_frequent_caller") == "Bob"

def test_4():
    logs = [
        {"name": "Alice", "duration": 400},
        {"name": "Bob", "duration": 200},
        {"name": "Alice", "duration": 200},
        {"name": "Bob", "duration": 400},
        {"name": "Charlie", "duration": 400}
    ]
    assert solution.process_call_logs(logs, "most_frequent_caller") == "Alice"
