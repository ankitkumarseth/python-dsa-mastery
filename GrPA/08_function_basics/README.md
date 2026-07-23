# GrPA Function Basics

You are required to complete the following functions to perform various operations on tuples and lists.

### Functions to Implement

* **`swap_halves(items)`**: Swap the first and second halves of a tuple with an even length.
### Examples
**Input:**
```python
swap_halves((1, 2, 3, 4, 5, 6))
```
**Output:**
```text
(4, 5, 6, 1, 2, 3)
```

* **`swap_at_index(items, k)`**: Break a tuple at a given index `k` (the element at the `k`-th index is included in the first half before swapping) and swap the parts.
### Examples
**Input:**
```python
swap_at_index((1, 2, 3, 4, 5, 6), 1)
```
**Output:**
```text
(3, 4, 5, 6, 1, 2)
```

* **`rotate_k(items, k=1)`**: Create a new sequence with elements of the given list moved `k` positions towards the right. The elements at the end should come back to the beginning in a circular order.
### Examples
**Input:**
```python
rotate_k((1, 2, 3, 4, 5, 6), 4)
```
**Output:**
```text
(3, 4, 5, 6, 1, 2)
```

* **`first_and_last_index(items, elem)`**: Get the indices of the first and last occurrence of a given item in a list. Assume the item is present in the list at least once.
### Examples
**Input:**
```python
first_and_last_index((1, 2, 3, 1, 5, 6), 1)
```
**Output:**
```text
(0, 3)
```

* **`reverse_first_and_last_halves(items)`**: Reverse the first and last halves of a list with even length **in place**.
### Examples
**Input:**
```python
reverse_first_and_last_halves([1, 2, 3, 4, 5, 6, 7, 8])
```
**Output:**
```text
[4, 3, 2, 1, 8, 7, 6, 5]
```
