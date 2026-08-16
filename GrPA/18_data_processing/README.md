# GrPA 18 - Data Processing

This module focuses on processing structured and unstructured data, including matrices, dictionaries, and standard string inputs.

## Find the index of the row with maximum number of zeros in a matrix
Given an `m x n` matrix, find the index of the row with the maximum number of zeros. Assume there will be only one row with the maximum number of zeros.

### Example
**Input:**
```python
[
    [1,0,1,4,1],
    [1,5,1,1,2],
    [2,0,2,0,3],
    [3,0,0,0,4],
]
```
**Output:**
```python
3
```
**Explanation:** The 4th row (index 3) has the maximum number of zeros (4 zeros).

## Given a dictionary of students and courses taken, sort the courses based on enrollment
Given a dictionary of student roll numbers with the list of courses they chose, find the courses sorted from the most number of enrollments to the least.
Assume no courses will have the same number of students enrolled.

### Example
**Input:**
```python
{
    '101': ['Math', 'Science'],
    '102': ['Math'],
    '103': ['Science', 'Math'],
    '104': ['Math', 'History'],
    '105': ['English', 'History', 'Science']
}
```
**Output:**
```python
['Math', 'Science', 'History', 'English']
```

## Find largest sub sequence with the antakshari property
The input is in multiple lines. The first line contains a positive integer `n`. This is followed by `n` lines, each containing sequences of words. Each line thus consists of multiple words, separated by commas, with no spaces in between words.

You have to output, for each line, the length of the longest subsequence of words following the antakshari property. Assume all words are lowercase.

A sub-sequence is a subset of consecutive words in this sequence. A sub-sequence is said to have the antakshari property if the last letter of every word is equal to the first letter in the next word in the sequence.

### Example
**Input:**
```text
2
one,two,order,real,long,tight,tree,cool,lot,trouble
ant,tree,ear,rat,tower,retail
```
**Output:**
```text
4
6
```
**Explanation:**
- First sequence: `two`, `order`, `real`, `long` (length 4)
- Second sequence: `ant`, `tree`, `ear`, `rat`, `tower`, `retail` (length 6)

## Hyphen seperated word digits of a number
Given an integer, generate a string with its digits as words separated by hyphens.

### Example
**Input:**
```python
123
```
**Output:**
```python
"one-two-three"
```
