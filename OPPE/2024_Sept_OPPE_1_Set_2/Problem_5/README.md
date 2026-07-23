# Find Sum and Absolute Difference Alternately

Given `n` pairs of integers, print the sum and the absolute difference of each pair alternatively, starting with the sum for the first pair.

**NOTE:** This is an I/O type question, you need to write the whole code for taking input and printing the output.

### Input Format
- The first line contains an integer `n`, the number of pairs.
- The next `n` lines each contain two comma-separated integers.

### Output Format
- For each pair of integers, print the sum if it is an odd-numbered pair (starting from 1), and the absolute difference if it is an even-numbered pair.

### Examples

**Input:**
```
3
1,2
3,5
4,3
```
**Output:**
```
3
2
7
```

**Explanation**
1. First pair `(1, 2)`: Sum (1 + 2 = 3)
2. Second pair `(3, 5)`: Absolute difference (|3 - 5| = 2)
3. Third pair `(4, 3)`: Sum (4 + 3 = 7)
