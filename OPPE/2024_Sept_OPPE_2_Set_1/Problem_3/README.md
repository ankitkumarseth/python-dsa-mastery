# Check if the given element is present in opposite halves

Write a function `is_present_in_opposite_halves(elem, l1: list, l2: list)` that checks whether the given `elem` is present in opposite halves of the two lists `l1` and `l2`.
The function should return `True` if the element exists in one half of `l1` and in the opposite half of `l2`, and `False` otherwise.

Note that both the below cases are valid and evaluate to `True`:
- `elem` in the first half of `l1` and second half of `l2`
- `elem` in the second half of `l1` and first half of `l2`

Assume both lists `l1` and `l2` have even lengths.

**NOTE:** This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

### Examples

**Input:**
```python
is_present_in_opposite_halves(3, [1, 2, 3, 4], [5, 6, 3, 8])
```
**Output:**
```python
False
```
*(3 is in the second half of l1 and the second half of l2)*

**Input:**
```python
is_present_in_opposite_halves(7, [1, 2, 3, 4], [5, 6, 3, 8])
```
**Output:**
```python
False
```
*(7 is not in l1 or l2)*

**Input:**
```python
is_present_in_opposite_halves(6, [5, 6, 7, 8], [1, 2, 6, 4])
```
**Output:**
```python
True
```
*(6 is in the first half of l1 and the second half of l2)*

**Input:**
```python
is_present_in_opposite_halves(6, [5, 7, 6, 8], [1, 6, 2, 4])
```
**Output:**
```python
True
```
*(6 is in the second half of l1 and the first half of l2)*
