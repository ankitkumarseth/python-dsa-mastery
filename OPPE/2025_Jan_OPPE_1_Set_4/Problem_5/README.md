# Compute Running Average Skipping NaN

Read numbers from the input until the line `END` and print the running average after adding each number as float with one decimal place. If `NaN` is encountered, ignore it and do not take it into account or print anything for that.

Running Average is the average of the numbers encountered so far.

Use `round(num,1)` for printing the average.

**NOTE:** This is an I/O type question, you need to write the whole code for taking input and printing the output.

### Example

**Input:**
```
2
4
6
NaN
8
END
```
**Output:**
```
2.0
3.0
4.0
5.0
```
**Explanation:**
The average with 2 is just 2, so `2.0`
The average of 2 and 4 is 3, `3.0`
The average of 2, 4 and 6 is (2+3+6)/3 = `4.0`
The fourth line is NaN this nothing is updated or printed.
The average is (2+4+6+8)/4 = `5.0`
