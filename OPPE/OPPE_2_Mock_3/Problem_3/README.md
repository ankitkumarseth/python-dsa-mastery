# Best Performers

You are given a list of dictionaries `overs` where each dictionary corresponds to a single over bowled by a bowler. Each over contains:
- Bowler name as key.
- Value associated with this key is a list of events for the over, where each event could be:
  - An integer value `{1, 2, 3, 4, 6}` indicating runs scored on that ball.
  - `'W'` indicating a wicket taken on that ball.
  - `'Wd'` indicating a wide ball, which incurs 1 extra run.
  - `'Nb[i]'` indicating a no-ball, where `i` represents runs scored on that ball, and incurs 1 extra run in addition to the runs from the no-ball itself.

Each over has 6 valid balls (ie. excluding extras like wide and no-balls).

One of the entry is given for your reference:
`{'Ashwin': [1, 1, 0, 'W', 'Wd', 6, 'Nb[4]', 0]}`
Here, 'Ashwin' gave 14 runs in the over and took 1 wicket.
`1 + 1 + 0 + 1(extra: wide) + 6 + 5(extras: noball) + 0 = 14`

Define a function named `best_performers`, that accepts `overs` as argument and returns a list of best bowlers based on their performances.

Bowlers are sorted on the basis of most wickets taken. If two bowlers have taken same number of wickets, then the best performer among them is decided on the basis of lower economy rate.
Economy Rate: Defined as the total runs conceded (including extras) divided by the total number of overs bowled by the bowler. Round the economy rate upto two decimal places.

### Example
```python
overs = [
    {'Bumrah': [1, 2, 'W', 0, 2, 'Wd', 0]},
    {'Shami': ['Nb[4]', 2, 1, 0, 'W', 'Wd', 'Wd', 4, 0]},
    {'Ashwin': [1, 4, 0, 3, 2, 1]}, 
    {'Shami': ['W', 2, 0, 0, 'Wd', 2, 6]},
    {'Bumrah': ['W', 'W', 1, 1, 0, 0]} 
]

best_performers(overs)
# Output
# [('Bumrah', 3, 4.0), ('Shami', 2, 12.5), ('Ashwin', 0, 11.0)]
```
