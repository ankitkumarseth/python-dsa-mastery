# Problem 4

Given an initial balance and a series of daily transactions, find the minimum balance, maximum balance, and balance at the end of the day for each day. The input will consist of multiple lines where the first line gives the number of days, the second line gives the initial balance, and each subsequent line represents the transactions for one day. The final balance of the previous day will be the initial balance of the current day.

## Input

The first line contains an integer n, the number of days.
The second line contains an integer initial_balance, the initial balance for the first day.
Each of the next n lines contains a space-separated list of integers representing transactions for that day.

## Output

For each day, print the minimum balance, maximum balance, and current balance as a comma-separated string.

### Examples
**Input:**
```
2
150
-10 10 -10 5
20 -20 30 -10
```
**Output:**
```
140,150,145
145,175,165
```
**Explanation**

Day 1:

Initial balance: 150
Transactions: -10, 10, -10, 5
Calculations:

Balance after -10: 140
Balance after +10: 150
Balance after -10: 140
Balance after +5: 145
Min balance: 140 Max balance: 150 Current Balance: 145

Output for Day 1: 140,150,145

Day 2:

Initial balance (end balance of Day 1): 145
Transactions: 20, -20, 30, -10
Calculations:

Balance after +20: 165
Balance after -20: 145
Balance after +30: 175
Balance after -10: 165
Min balance: 145 Max balance: 175 Current Balance: 165

Output for Day 2: 145,175,165
