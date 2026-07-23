# Check if 2D Vectors are Orthogonal

Write a function `are_orthogonal` that takes two tuples `t1` and `t2` as input. Each tuple represents a 2D vector with two elements `(x, y)`. The function should return `True` if the vectors are orthogonal (perpendicular), and `False` otherwise.

Hint: Two vectors are orthogonal if their dot product is zero. Dot product is the sum of product of the corresponding elements in the vectors.

**NOTE:** This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

### Examples

```python
>>> are_orthogonal((1, 2), (12, -6)) # 1*12 + 2*(-6) = 0, equal to zero
True 
>>> are_orthogonal((2, 0), (4, 1)) # 2*4 - 1*0 = 8, not equal to zero
False
>>> are_orthogonal((0, 5), (-5, 0)) # 0*(-5) - 5*0 = 0, equal to zero
True
```
