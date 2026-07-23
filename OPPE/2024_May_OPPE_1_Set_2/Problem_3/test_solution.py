import os, importlib.util
SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_teams():
    batsmen = [
        {'name': 'Batsman1', 'runs': 50, 'team': 'TeamA'},
        {'name': 'Batsman2', 'runs': 30, 'team': 'TeamB'},
        {'name': 'Batsman3', 'runs': 70, 'team': 'TeamA'},
        {'name': 'Batsman4', 'runs': 40, 'team': 'TeamC'},
        {'name': 'Batsman5', 'runs': 60, 'team': 'TeamB'}
    ]
    assert solution.top_k_teams(batsmen, 2) == ['TeamA', 'TeamB']
