# Swap Every Alternate Line and Reverse Odd Lines

Given multiple lines of input, modify the lines as follows:
- Swap every two consecutive lines.
- Reverse every odd-numbered line in the output sequence.

**NOTE:** This is an I/O type question, you need to write the whole code for taking input and printing the output.

### Input Format:
- The first line contains the integer `n`, the number of lines.
- The next `n` lines contain text strings.

### Output Format:
- Print the transformed lines according to the rules specified.

### Examples

**Input:**
```
5
apple
orange
pineapple
mango
kiwi
```
**Output:**
```
egnaro
apple
ognam
pineapple
iwik
```

**Explanation:**
- The first and second lines are swapped, with the first line (orange) reversed.
- The third and fourth lines are swapped, with the third line (mango) reversed.
- The fifth line (kiwi), being alone, is reversed.
