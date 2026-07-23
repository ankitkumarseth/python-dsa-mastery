# Increment Value of Key in Dict with Max Limit

Write a function `increment_value_with_max_limit` that increments the value for a specified key in a dictionary by a given increment value (`inc`). However, the value should not exceed a specified maximum limit (`limit`).

Assume the dictionary values are integers. If the resulting value after incrementing is greater than the limit, it should be capped at the limit.

**NOTE:** This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

### Examples

**Input:**
```python
d = {"x": 5, "y": 3, "z": 5}
key, inc, limit = "y", 5, 5
increment_value_with_max_limit(d, key, inc, limit)
```
**Output:**
```python
{"x": 5, "y": 5, "z": 5}
```
*(3+5=8 but max limit is 5)*

**Input:**
```python
increment_value_with_max_limit(d, "z", 5, 11)
```
**Output:**
```python
{"x": 5, "y": 5, "z": 10}
```
*(5+5=10 less than limit)*

**Input:**
```python
increment_value_with_max_limit(d, "x", 5, 4)
```
**Output:**
```python
{"x": 4, "y": 5, "z": 10}
```
*(4+5=9 capped at max limit 4)*
