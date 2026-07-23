# Abbreviate Initials And Sort

Write a program that takes a list of full names and outputs their initials (except the last name) followed by the full last name. The output should be sorted alphabetically.

An initial is the first letter of each part of a name.

Assume that the names are given in the correct case.

*Hint: Use sorted function or list.sort to sort the list*

**NOTE:** This is an I/O type question, you need to write the whole code for taking input and printing the output.

### Input Format
- First line contains the number of names, `n`.
- Next `n` lines contain one full name per line.

### Output Format
- Output the processed names in sorted order, one per line.

### Examples

**Input:**
```
3
John Doe
Alice Johnson
Bob Alan Rickman
```
**Output:**
```
A. Johnson
B. A. Rickman
J. Doe
```
