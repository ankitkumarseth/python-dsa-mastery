# Ceil Marks to Nearest Tens if Close

Write a program to process roll numbers and marks for students. If a student's marks have a unit digit of 8 or 9, round their marks up to the nearest tens. Otherwise, keep the marks unchanged. Print only the roll number and updated marks for students whose marks were updated.

**NOTE:** This is an I/O type question, you need to write the whole code for taking input and printing the output.

### Input Format
- The first line contains the number of lines of student data `n`.
- Next `n` lines contains the student data with roll number and marks separated by space.

### Output Format
- Student data for the roll number whose marks has been updated in the format of roll number and marks separated by space.

### Examples

**Input:**
```
5
11 45
12 47
13 78
14 69
15 50
```
**Output:**
```
13 80
14 70
```

**Input:**
```
3
11 55
12 35
13 69
```
**Output:**
```
13 70
```

**Input:**
```
4
21 88
22 89
23 90
24 70
```
**Output:**
```
21 90
22 90
```
