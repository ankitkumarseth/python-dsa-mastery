# GrPA 17 - Collections

This module covers 4 distinct problems focusing on lists, tuples, and sets.

## Reverse First half in an even length tuple
Given an even-length tuple `t`, return a new tuple where the first half of the tuple is reversed, and the second half remains unchanged.

### Example
**Input:**
```python
t = (1, 2, 3, 4, 5, 6)
```
**Output:**
```python
(3, 2, 1, 4, 5, 6)
```
**Explanation:** The first half `(1, 2, 3)` is reversed to `(3, 2, 1)`.

## Delete the first three elements in a list
Given a list `l`, modify it in place by deleting the first three elements. If the list has fewer than three elements, delete all elements.

### Example
**Input:**
```python
l = [1, 2, 3, 4, 5]
```
**Output:**
```python
[4, 5]
```

## Number of unique common digits between two integers
Given two integers, return the number of unique digits that are common in both numbers.

### Example
**Input:**
```python
287498, 295424
```
**Output:**
```python
3
```
**Explanation:** `2`, `4` and `9` are common to both numbers.

## Find final position in 2d given initial position and velocity
Given an initial position of a point moving in a 2d cartesian plane with a constant velocity, find the the final position of the point after a given time in two dimensions.

*Hint: final position = intial position + velocity * time*

### Example
**Input:**
```python
pos = (1, 1), vel = (2, 2), time = 3
```
**Output:**
```python
(7, 7)
```
