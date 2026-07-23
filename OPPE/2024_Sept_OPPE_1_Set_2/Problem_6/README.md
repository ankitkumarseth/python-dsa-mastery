# Matrix Walk

Given a square matrix, walk along the matrix according to a specified path and return a list of elements based on the path.

**Paths:**
- `"L"`: Start from the top-left corner and traverse in an "L" shape.
- `"Z"`: Start from the top-left corner and traverse the matrix in a "Z" shape.
- `"O"`: Start from the top-left corner and traverse the matrix clockwise in an "O" shape.

**NOTE:** This is a function type question, you don't have to take input or print the output, just have to complete the required function definition. You can define helper functions if needed, but the actual solution should be in the given function template.

### Example

For matrix:
```python
M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
- **L-shape:** `[1, 4, 7, 8, 9]`
- **Z-shape:** `[1, 2, 3, 5, 7, 8, 9]`
- **O-shape:** `[1, 2, 3, 6, 9, 8, 7, 4]`

*(Note: "L" has 2 private test cases where "Z" and "O" has one private test case each)*
