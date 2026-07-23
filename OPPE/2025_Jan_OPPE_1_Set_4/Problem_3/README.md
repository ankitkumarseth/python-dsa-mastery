# Remove n Elements from the Given Index

Write a function `remove_n_elems_from_index` that takes a tuple `t`, an integer `n`, and an index `i` as input. The function should return a new tuple with the `n` elements starting at index `i` removed. If the index `i` is out of bounds, return the original tuple.

**NOTE:** This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

### Examples

```python
>>> remove_n_elems_from_index((1, 2, 3, 4, 5), 2, 1)
(1, 4, 5)
>>> remove_n_elems_from_index((10, 20, 30, 40, 50), 3, 2)
(10, 20)
>>> remove_n_elems_from_index((1, 2, 3, 4, 5), 5, 0)
()
```
