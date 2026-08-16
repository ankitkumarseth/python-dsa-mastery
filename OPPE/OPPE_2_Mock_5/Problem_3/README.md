# Sort Tuples

Sorts a list of tuples by the second element of each tuple. In case of a tie, sorts by the third element. In case of another tie, sorts by the first element.

### Example:
```python
>>> sort_tuples_by_second_then_third([(0,2,0),(1,2,1),(-6,2,1),(0,2,1),(-9,1,0),(5,2,-1)])
[(-9, 1, 0), (5, 2, -1), (0, 2, 0), (-6, 2, 1), (0, 2, 1), (1, 2, 1)]
```
