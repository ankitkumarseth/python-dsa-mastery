# Time Series Analysis

Given a list of numerical values, implement the following functions to analyze its trend:

- `difference(data: list) -> list`: Returns a list of differences between consecutive elements in the input list.
- `nth_order_difference(data: list, n: int) -> list`: Returns a list of nth order differences between consecutive elements in the input list.
- `has_positive_trend(data: list) -> bool`: Returns `True` if the list has a positive trend, `False` otherwise.
- `moving_average(data: list, window_size: int) -> list`: Returns a list of moving averages of the input data with the given window size.
- `has_negative_average_trend(data: list, window_size: int) -> bool`: Returns `True` if the list has a negative trend after applying a moving average with the given window size.

### Example

```python
data1 = [1, 3, 5, 7, 9]
data2 = [10, 8, 6, 4, 2]
data3 = [1, 2, 1, 0, -1]

print(has_positive_trend(data1))  # True
print(has_positive_trend(data3))  # False
print(difference(data1))           # [2, 2, 2, 2]
print(nth_order_difference(data1, 2))  # [0, 0, 0]
print(moving_average(data1, 3))    # [2.0, 4.0, 6.0, 8.0]
print(has_negative_average_trend(data2, 2))  # True
```

**Moving Average Example:**
```python
>>> l = [1,2,3,4,5,6,7,8,9] 
>>> window_size = 4
# [1,2,3,4] -> 10/4 -> 2.5
# [2,3,4,5] -> 14/4 -> 3.5
# [3,4,5,6] -> 18/4 -> 4.5
# [4,5,6,7] -> 22/4 -> 5.5
# [5,6,7,8] -> 26/4 -> 6.5
# [6,7,8,9] -> 30/4 -> 7.5
>>> moving_average(l, window_size)
[2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
```
