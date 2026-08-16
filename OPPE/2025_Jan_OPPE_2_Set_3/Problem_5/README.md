# Hand Cricket Match Runs

Given two columns of numbers from 0 to 6, separated by space, played by batsman and bowler in a hand cricket match, find the total number of balls played and the total runs scored by the batsman at the end of the innings.

- The match ends when the batsman plays the same number as the bowler or plays the same number twice continously.
- The number batsman plays will be added to the runs, except when batsman plays 0, the number bowler plays will be added to the runs.
- The number played when the game ends is not counted towards the runs.

### Input Format
Each line with numbers played by batsman and bowler separated by space.

### Output Format
Number of balls played and the total runs separated by space.

### Examples

**Input:**
```text
1 4
2 3
6 2
5 1
0 2
3 3
```
**Output:**
```text
6 16
```
**Explanation:**
- 1 4 -> 1
- 2 3 -> 2
- 6 2 -> 6
- 5 1 -> 5
- 0 2 -> 2 (0 played by batsman so 2 is counted as runs)
- 3 3 -> out
Total: 1+2+6+5+2 = 16

**Input:**
```text
1 4
5 3
0 3
5 1
5 4
```
**Output:**
```text
5 14
```
**Explanation:**
- 1 4 -> 1
- 5 3 -> 5
- 0 3 -> 3 (0 played by batsman so 3 is counted as runs)
- 5 1 -> 5
- 5 4 -> out (batsman played 5 twice continously)
Total: 1+5+3+5 = 14
