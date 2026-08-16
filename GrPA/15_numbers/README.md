# GrPA 15 - Numbers

This module covers 4 distinct problems focusing on number manipulation, dictionary creation, and coordinate mathematics.

## Seconds to Minute-Seconds
Given an integer `seconds`, return a tuple `(minutes, remaining_seconds)` where `minutes` is the number of full minutes in `seconds`, and `remaining_seconds` is the leftover seconds.

### Example
**Input:**
```python
125
```
**Output:**
```python
(2, 5)
```
**Explanation:** 125 seconds is 2 full minutes (120 seconds) and 5 leftover seconds.

## Create an Indexed Dictionary
Given a list of items, create a dictionary with the indices as keys and the items as values.

### Example
**Input:**
```python
["Alice", "Bob", "Charlie", "David"]
```
**Output:**
```python
{0: 'Alice', 1: 'Bob', 2: 'Charlie', 3: 'David'}
```

## Manhattan Distance via Point B
Given three points `a`, `b`, and `c` on the Cartesian plane, calculate the Manhattan distance to go from point `a` to point `c` via point `b`.
Manhattan distance is the sum of the absolute differences of their Cartesian coordinates.

### Example
**Input:**
```python
a = (1, 2)
b = (3, 4)
c = (6, 7)
```
**Output:**
```python
10
```
**Explanation:** 
- `a` to `b`: `abs(1-3) + abs(2-4) = 2 + 2 = 4`
- `b` to `c`: `abs(3-6) + abs(4-7) = 3 + 3 = 6`
- Total: `4 + 6 = 10`

## Right Triangle with Even Sides
Given three side lengths in the increasing order of length as `a`, `b`, and `c`, where `a<=b<=c`, check if the given sides are the sides of a right triangle whose perpendicular sides are of even length.

### Example 1
**Input:**
```python
a = 6, b = 8, c = 10
```
**Output:**
```python
True
```
**Explanation:** `6^2 + 8^2 = 10^2` (36 + 64 = 100). Both perpendicular sides (6 and 8) are even.

### Example 2
**Input:**
```python
a = 3, b = 4, c = 5
```
**Output:**
```python
False
```
**Explanation:** While `3^2 + 4^2 = 5^2`, one of the perpendicular sides (3) is not even.
