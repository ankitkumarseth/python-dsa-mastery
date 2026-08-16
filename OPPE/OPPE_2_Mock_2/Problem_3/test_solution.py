import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_get_leaderboard():
    matches1 = [
        {"team1": "Brazil", "team2": "Argentina", "goals1": 2, "goals2": 1},
        {"team1": "Germany", "team2": "France", "goals1": 1, "goals2": 2},
        {"team1": "Brazil", "team2": "Germany", "goals1": 3, "goals2": 2},
        {"team1": "Argentina", "team2": "France", "goals1": 1, "goals2": 1},
        {"team1": "Brazil", "team2": "France", "goals1": 1, "goals2": 0},
        {"team1": "Argentina", "team2": "Germany", "goals1": 2, "goals2": 0},
        {"team1": "Germany", "team2": "France", "goals1": 0, "goals2": 1}
    ]
    assert solution.get_leaderboard(matches1) == [
        ('Brazil', 6, 6),
        ('France', 5, 4),
        ('Argentina', 3, 4),
        ('Germany', 0, 3)
    ]

    matches2 = [
        {"team1": "Spain", "team2": "Italy", "goals1": 2, "goals2": 2},
        {"team1": "England", "team2": "Spain", "goals1": 1, "goals2": 1},
        {"team1": "Italy", "team2": "England", "goals1": 0, "goals2": 3},
        {"team1": "Spain", "team2": "Italy", "goals1": 1, "goals2": 0},
        {"team1": "England", "team2": "Italy", "goals1": 2, "goals2": 2},
        {"team1": "Spain", "team2": "England", "goals1": 1, "goals2": 1},
    ]
    assert solution.get_leaderboard(matches2) == [
        ("England", 5, 7),
        ("Spain", 5, 5),
        ("Italy", 2, 4)
    ]
