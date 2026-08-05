# GrPA Composing Functions

Implement the following functions to solve various path-traversal problems on a matrix.

### Setup
You are given a matrix of size `m x n` consisting of ones (`1`) and zeros (`0`). There is a single continuous path formed with ones that starts from the **rightmost cell in the last row** (m-th row) with `1` and ends at the **leftmost cell in the first row** with `1` in it. The path does not branch, and there is only one such path. The path can move vertically and horizontally.

### Functions to Implement

* **`index_of_first_occurance(row: list, elem)`**: Find the index of the first occurrence of an element in a list.
### Examples
**Input:**
```python
index_of_first_occurance([0, 0, 1, 1, 0], 1)
```
**Output:**
```text
2
```

* **`index_of_last_occurance(row: list, elem)`**: Find the index of the last occurrence of an element in a list. (Hint: use `index_of_first_occurance` with reversal).
### Examples
**Input:**
```python
index_of_last_occurance([0, 0, 1, 1, 0], 1)
```
**Output:**
```text
3
```

* **`is_valid_coordinate(x: int, y: int, M)`**: Checks if `x, y` is a valid coordinate (indices) in the matrix `M` (list of list). Assume coordinates are non-negative.
### Examples
**Input:**
```python
matrix = [
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0]
]
print(is_valid_coordinate(2, 2, matrix))
print(is_valid_coordinate(2, 5, matrix))
print(is_valid_coordinate(5, -2, matrix))
```
**Output:**
```text
True
False
False
```

* **`valid_adjacent_coordinates(x: int, y: int, M)`**: Create a set of valid adjacent coordinates (indices) given `x, y` and a matrix `M`.
### Examples
**Input:**
```python
valid_adjacent_coordinates(2, 2, matrix)
```
**Output:**
```text
{(1, 2), (2, 1), (2, 3), (3, 2)}
```

* **`next_coordinate_with_value(curr_coords, value, M, prev_coords=None)`**: Find the coordinate of the next cell that has the `value` in it. For the starting coordinate, `prev_coords` would be `None`.
### Examples
**Input:**
```python
next_coordinate_with_value((2, 2), 1, matrix, (2, 1))
```
**Output:**
```text
(2, 3)
```

* **`get_path_coordinates(M)`**: Given the matrix `M`, find the path formed by `1`s from the last row to the first row as a list of tuples.
### Examples
**Input:**
```python
matrix = [
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0]
]
get_path_coordinates(matrix)
```
**Output:**
```python
[(4, 1), (4, 0), (3, 0), (2, 0), (2, 1), (2, 2), (2, 3), (1, 3), (0, 3), (0, 2)]
```
* **`print_path(M)`**: Traverse along the path and print the coordinates from start to end as tuples over multiple lines.
### Examples
**Input:**
```python
matrix = [
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0]
]
print_path(matrix)
```
**Output:**
  > ```text
  > (4, 1)
  > (4, 0)
  > (3, 0)
  > (2, 0)
  > (2, 1)
  > (2, 2)
  > (2, 3)
  > (1, 3)
  > (0, 3)
  > (0, 2)
  > ```

* **`alternate_path(M)`**: While going in the path, flip every `1` in the **even positions** in the path (0th, 2nd, 4th, etc.) to `2`. Modify the matrix **inplace**.
### Examples
**Input:**
```python
matrix = [
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0]
]
alternate_path(matrix)
```
**Output State:**
  > ```python
  > [
  >     [0, 0, 2, 1],
  >     [0, 0, 0, 2],
  >     [2, 1, 2, 1],
  >     [1, 0, 0, 0],
  >     [2, 1, 0, 0]
  > ]
  > ```

* **`count_path(M)`**: Instead of flipping, put the count of the step (starting from 1) in the path. Modify the matrix **inplace**.
### Examples
**Input:**
```python
matrix = [
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0]
]
count_path(matrix)
```
**Output State:**
  > ```python
  > [
  >     [0, 0, 10, 9],
  >     [0, 0, 0, 8],
  >     [4, 5, 6, 7],
  >     [3, 0, 0, 0],
  >     [2, 1, 0, 0]
  > ]
  > ```

* **`mirror_horizontally(M)`**: Also add a path that is the **horizontal mirror** of the original path in the same matrix. Modify the matrix **inplace**.
### Examples
**Input:**
```python
matrix = [
  [0, 1, 0, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 0, 1, 0],
  [0, 0, 0, 1, 1]
]
```
**Output:**
```python
[
  [0, 1, 0, 1, 0],
  [0, 1, 1, 1, 0],
  [0, 1, 0, 1, 0],
  [1, 1, 0, 1, 1]
]
```

* **`mirror_vertically(M)`**: Also add a path that is the **vertical mirror** of the original path in the same matrix. Modify the matrix **inplace**.
### Examples
**Input:**
```python
matrix = [
  [0, 1, 0, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 0, 1, 0],
  [0, 0, 0, 1, 1]
]
mirror_vertically(matrix)
```
**Output State:**
  > ```python
  > [
  >   [0, 1, 0, 1, 1],
  >   [0, 1, 1, 1, 0],
  >   [0, 1, 1, 1, 0],
  >   [0, 1, 0, 1, 1]
  > ]
  > ```
