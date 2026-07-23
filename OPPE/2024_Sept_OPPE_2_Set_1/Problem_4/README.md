# Count Odd 3 Digit Numbers (Ignore None)

Write a function `count_odd_three_digit_nums(nums)` that takes a list of integers `nums` and returns the count of numbers that are:
- Odd.
- Three-digit numbers (ignoring the negative sign if present).
- Not `None`.

**NOTE:** This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

### Examples

**Input:**
```python
count_odd_three_digit_nums([101, -203, None, 99, 300])
```
**Output:**
```python
2
```
*(101 and -203 are odd three-digit numbers, ignoring None)*

**Input:**
```python
count_odd_three_digit_nums([None, 120, 301, -401, 78])
```
**Output:**
```python
2
```
*(301 and -401 qualify as odd three-digit numbers)*

**Input:**
```python
count_odd_three_digit_nums([10, 305, 507, 99])
```
**Output:**
```python
2
```
*(305 and 507 qualify as odd three-digit numbers)*
