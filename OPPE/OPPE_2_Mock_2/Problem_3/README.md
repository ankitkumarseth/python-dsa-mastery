# Leaderboard Generation

You are given a list of dictionaries `matches` where each element of the list would correspond to a match result. Each match result contains the team involved, the winner and the goals scored by the winner team. One of the entry is given below for your reference:

`{'team1': 'Brazil', 'team2': 'Argentina', 'goals1': 2, 'goals2': 1}`

Define a function named `get_leaderboard`, that takes `matches` as input and returns the leaderboard.

Teams are sorted by their total points. Points are awarded as follows:
- Win : 2 pts.
- Draw: 1 pts.
- Loss: 0 pts.

If the teams have same points, then they should be sorted on the basis of the number of goals scored.

### Example
```python
matches = [
    {"team1": "Brazil", "team2": "Argentina", "goals1": 2, "goals2": 1},
    {"team1": "Germany", "team2": "France", "goals1": 1, "goals2": 2},
    {"team1": "Brazil", "team2": "Germany", "goals1": 3, "goals2": 2},
    {"team1": "Argentina", "team2": "France", "goals1": 1, "goals2": 1},
    {"team1": "Brazil", "team2": "France", "goals1": 1, "goals2": 0},
    {"team1": "Argentina", "team2": "Germany", "goals1": 2, "goals2": 0},
    {"team1": "Germany", "team2": "France", "goals1": 0, "goals2": 1}
]

get_leaderboard(matches)
# Output
# [('Brazil', 6, 6), ('France', 5, 4), ('Argentina', 3, 4), ('Germany', 0, 3)]
```
