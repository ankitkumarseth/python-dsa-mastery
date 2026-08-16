# Abbreviate Initials And Sort

Write a Python function that takes a list of full names, processes them to create abbreviated forms in the format "Last, F.M." (where F and M are the initials of the first and middle names), and returns the list sorted alphabetically.

Assume that the names are given in the correct case.

*Hint: Use `sorted` function or `list.sort` to sort the list*

NOTE: This is an I/O type question, you need to write the whole code for taking input and printing the output.

### Input Format
First line contains the number of names, `n`.
Next `n` lines contain one full name per line.

### Output Format
Output the processed names in sorted order, one per line.

### Example

**Input:**
```text
3
John Doe
Alice Johnson
Bob Alan Rickman
```

**Output:**
```text
Doe, J.
Johnson, A.
Rickman, B.A.
```
