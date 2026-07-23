# Swap the Last Chars in Dictionary Values

Write a function that swaps the last characters of the values corresponding to two specified keys in a dictionary.

Assume that the values in the dictionary are strings.

### Input:
- A dictionary `d` where the values are strings.
- Two keys `k1` and `k2`.

### Output:
- Modify the dictionary in-place by swapping the last characters of the values of the given keys.
- The function returns `None` as it modifies the dictionary directly.
- Assume the values for both keys `k1` and `k2` are non-empty strings and the dictionary contains the keys `k1` and `k2`.

**NOTE:** This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

### Examples

**Example 1:**
```python
d = {"first": "apple", "second": "mango", "third":"banana"}
swap_last_chars_of_values(d, "first", "second")
d
```
**Output:**
```python
{'first': 'applo', 'second': 'mange', 'third': 'banana'}
```

**Example 2:**
```python
d = {"key1": "hello", "key2": "world"}
swap_last_chars_of_values(d, "key1", "key2")
d
```
**Output:**
```python
{'key1': 'helld', 'key2': 'worlo'}
```
