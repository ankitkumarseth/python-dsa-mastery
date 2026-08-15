# Problem 3

Given a list of dictionaries where each dictionary contains a batsman's `name`, `runs`, and `team`, write a function `top_k_teams(batsmen, k)` that returns the top `k` teams with the highest total aggregated runs.

### Example Input
```python
batsmen = [
    {'name': 'Batsman1', 'runs': 50, 'team': 'TeamA'},
    {'name': 'Batsman2', 'runs': 30, 'team': 'TeamB'},
    {'name': 'Batsman3', 'runs': 70, 'team': 'TeamA'},
    {'name': 'Batsman4', 'runs': 40, 'team': 'TeamC'},
    {'name': 'Batsman5', 'runs': 60, 'team': 'TeamB'}
]
k = 2
```

### Example Output
```python
['TeamA', 'TeamB']
```

### Explanation
- **TeamA**: 50 + 70 = 120 runs
- **TeamB**: 30 + 60 = 90 runs
- **TeamC**: 40 runs
The top `2` teams by total runs are `TeamA` and `TeamB`.
