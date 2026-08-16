# Remainder Grouping Dictionary

Write a Python program that reads two inputs from the user:
1. A single line containing a list of integers separated by commas. The line may contain arbitrary spaces around the commas.
2. An integer `k` - the divisor.

Your task is to build a dictionary that groups the numbers by their remainder when divided by `k`.
- Each key is a remainder `r` (`0 <= r < k`) that actually appears among the given numbers.
- The value for a key `r` is a list of all numbers whose remainder equals `r`, sorted in ascending order.

Print the dictionary in ascending order of the keys using the following format (one key per line) with values in ascending order:
```text
key1 - val1,val2,...
key2 - val1,val2,...
...
```
There must be no extra spaces around the dash or the commas.

NOTE: This is a standard input/output type problem. Read from standard input and print to standard output.

### Examples

**Input:**
```text
1,2,3,4,5,6
3
```
**Output:**
```text
0 - 3,6
1 - 1,4
2 - 2,5
```

**Input:**
```text
45,53,10,21,33
5
```
**Output:**
```text
0 - 45,10
1 - 21
3 - 53,33
```
