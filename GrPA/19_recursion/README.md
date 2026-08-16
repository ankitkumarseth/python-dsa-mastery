# GrPA 19 - Recursion and Binary Search

This module focuses on solving problems cleanly by strictly using recursion instead of iterative loops. 

## Reverse a List
Write a recursive function named `reverse` that accepts a list `L` as argument and returns the reversed list.

### Example
**Input:**
```python
[10, 5, 1, 4, 9]
```
**Output:**
```python
[9, 4, 1, 5, 10]
```

## Linear Proportionality Check
Write a recursive function named `linear` that accepts the following arguments:
- `P`: a non-empty list of positive integers
- `Q`: a non-empty list of positive integers
- `k`: a positive integer

It should return `True` only if both the conditions given below are satisfied:
1. `P` and `Q` are of same length.
2. `P[i] = k * Q[i]`, for every integer `i` in the range `[0, len(P)-1]`, endpoints inclusive.

### Example
**Input:**
```python
P = [2, 4, 6, 8]
Q = [1, 2, 3, 4]
k = 2
```
**Output:**
```python
True
```

## The Collatz Conjecture
The Collatz function is defined for a positive integer `n` as follows:
- `f(n) = 3n + 1` if `n` is odd
- `f(n) = n / 2` if `n` is even

We consider the repeated application of the Collatz function starting with a given integer `n`, which results in a sequence. It is conjectured that no matter which positive integer `n` you start from, the sequence will always reach `1`. 

For example, if `n = 10`, the sequence is:

| Seq No. | n | f(n) |
| --- | --- | --- |
| 1 | 10 | 5 |
| 2 | 5 | 16 |
| 3 | 16 | 8 |
| 4 | 8 | 4 |
| 5 | 4 | 2 |
| 6 | 2 | 1 |

Thus, if you start from `10`, you need to apply the function `f` six times in order to first reach `1`. Write a recursive function named `collatz` that accepts a positive integer `n` as argument, and returns the number of times `f` has to be applied repeatedly in order to first reach 1.

### Example
**Input:**
```python
7
```
**Output:**
```python
16
```

## Climbing Steps (Fibonacci)
Fibonacci likes to climb the steps either one at a time, two at a time or three at a time. He wants to find the total number of ways in which he can climb `n` steps, assuming that the order of his individual steps matters. 

For example, if he wishes to climb three steps, the case of `n = 3`, he could do it in four different ways:
- `(1, 1, 1)`: do it in three moves, one step at a time
- `(1, 2)`: do it in two moves, first take a single step, then a double step
- `(2, 1)`: do it in two moves, first take a double step, then a single step
- `(3)`: do it in just one move, directly leaping to the third step

Write a recursive function named `steps` that accepts a positive integer `n` as argument. It should return the total number of ways in which Fibonacci can ascend `n` steps. 

### Example
**Input:**
```python
5
```
**Output:**
```python
13
```

## Ancestry Tracing
`P` is a dictionary of father-son relationships that has the following structure: for any key in the dictionary, its corresponding value is the father of key. 

```python
P = {
    'Jahangir': 'Akbar', 
    'Akbar': 'Humayun', 
    'Humayun': 'Babur'    
}
```

Write a recursive function named `ancestry` that accepts the dictionary `P`, the `present` name of a person, and the `past` name of a person. It should return the sequence of ancestors of the person named `present`, traced all the way back up to person named `past`. 

### Example
**Input:**
```python
P = {'Anil': 'Krishna', 'Mohan': 'Prasanna', 'Krishna': 'Prasanna', 'Prasanna': 'Mukesh'}
present = 'Anil'
past = 'Prasanna'
```
**Output:**
```python
['Anil', 'Krishna', 'Prasanna']
```
