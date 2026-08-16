# Add average key with absolute difference value (in-place)

Write a function `add_average_key_diff(d, k1, k2)` that receives a dictionary `d` and two existing keys `k1` and `k2`.

The function should:
1. Compute the average of the two keys and round it to the nearest integer (use Python's builtin `round`).
2. Compute the absolute difference between the values stored for `k1` and `k2`.
3. Insert a new entry `average_key : absolute_difference` into `d`.
4. Do not return anything, the dictionary is modified in-place.

Assume `k1` and `k2` are present in `d` and their values are numeric (int or float). The new key is stored as an int.

NOTE: This is a function-type question, you only need to implement the function, no input/output handling is required.

### Example
```python
>>> d = {2: 10, 8: 30}
>>> add_average_key_diff(d, 2, 8)
>>> d
{2: 10, 8: 30, 5: 20}
```
