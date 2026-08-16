# PPA - Recursion and Binary Search

This module contains 14 practical programming assignments covering recursion, sequence processing, and search algorithms.

## 1. Triangular Number
Write a recursive function named `triangular` that accepts a positive integer `n` as argument and returns the sum of the first `n` positive integers.

### Example
**Input:** `5`  
**Output:** `15`

## 2. Factorial
Write a recursive function named `factorial` that accepts a positive integer `n` as argument and returns the factorial of `n`.

### Example
**Input:** `5`  
**Output:** `120`

## 3. Recursive Multiplication
Write a recursive function named `multiply` that accepts two positive integers `a` and `b` as argument and returns their product. You can only use `+` and `-` operators. You are not allowed to use the `*` symbol anywhere in your code!

### Example
**Input:** `5, 4`  
**Output:** `20`

## 4. Base 2 Logarithm
Write a recursive function named `logarithm` that accepts a positive integer `x` (which is a power of 2) as argument and returns `log2(x)`. Use of Python's standard libraries is not allowed.

### Example
**Input:** `16`  
**Output:** `4`

## 5. Palindrome Check
Write a recursive function named `palindrome` that accepts a string `word` as argument and returns `True` if it is a palindrome and `False` otherwise.

### Example
**Input:** `mom`  
**Output:** `True`

## 6. Semicircle Spiral Coordinates
Consider a spiral of semicircles. We start at a point `P_0` on the x-axis with coordinates `(l, 0)`. The first arm of the spiral ends at `P_1` with coordinates `(r, 0)`. The second arm starts at `P_1` and ends at the center of the first arm, `P_2`. The third arm starts from `P_2` and ends at `P_3` which is the center of the second arm, and so on.

Write two functions named `spiral_iterative` and `spiral_recursive` to compute the x-coordinate of the nth arm of the spiral.

### Example
**Input:** `left=0, right=1, n=4`  
**Output:** `0.625`

## 7. Count Occurrences
Write a recursive function named `count` that accepts a list of words `L` and a `word`. It should return the number of occurrences of `word` in `L`. You cannot use the built-in count method for lists.

### Example
**Input:** `L=['good', 'string', 'good', 'again', 'good'], word='good'`  
**Output:** `3`

## 8. Non-Decreasing List Check
Write a recursive function named `non_decreasing` that accepts a non-empty list `L` of integers and returns `True` if the elements are sorted in non-decreasing order from left to right.

### Example
**Input:** `[1, 10, 100, 1000]`  
**Output:** `True`

## 9. Unique Elements (Retain Last Occurrence)
Write a recursive function named `uniq` that accepts a non-empty list `L` as argument and returns a new list after removing all duplicates from it. Your function must retain the *last occurrence* of each distinct element in the list.

### Example
**Input:** `[10, 9, 6, 9, 10, 6, 10]`  
**Output:** `[9, 6, 10]`

## 10. Binary Search
Write a recursive function named `search` that accepts a sorted list of integers `L` and an integer `k`. Return `True` if `k` is found, and `False` otherwise.

### Example
**Input:** `L=[10, 20, 30, 40, 50], k=15`  
**Output:** `False`

## 11. Insertion Sort
1. Write a function named `insert` that accepts a sorted list `L` of integers and an integer `x`. It should return a sorted list with the element `x` inserted at the right place.
2. Write a recursive function named `isort` that accepts a non-empty list `L`. It should return a sorted list in ascending order. `isort` must make use of `insert`.

### Example
**Input:** `L=[1, 5, 4, 3, 2]`  
**Output:** `[1, 2, 3, 4, 5]`

## 12. Polynomial Evaluation
A polynomial can be represented using a list of its coefficients: `L = [a_0, a_1, a_2, ..., a_n]`.
Write a recursive function named `poly` that accepts the list of coefficients `L` and a real number `x_0`. Return the polynomial evaluated at `x_0`.

### Example
**Input:** `L=[1, 2, 3], x_0=5`  
**Output:** `86` (1 + 2*5 + 3*25)

## 13. Matrix Power
Write a recursive function named `power` that accepts a square matrix `A` (list of lists) and a positive integer `m`. Return `A^m`.

### Example
**Input:** `A=[[1,2,3], [4,5,6], [7,8,9]], m=3`  
**Output:** 
```python
[[468,576,684],
 [1062,1305,1548],
 [1656,2034,2412]]
```

## 14. Subset Sum (Coin Locker)
Write a recursive function named `subset_sum` that accepts a list of positive integers `L` (coins) and a positive integer `s` (target value). Return `True` if you can withdraw some subset of coins whose combined worth is `s`.

### Example
**Input:** `L=[1, 49, 29, 13, 95, 32, 10, 1, 5], s=21`  
**Output:** `False`
