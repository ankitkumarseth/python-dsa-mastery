# Check if a Triangle is Obtuse

Given two angles of a triangle (`theta_1` and `theta_2`) in degrees, determine if the triangle is obtuse. A triangle is obtuse if it has one angle greater than 90 degrees.

### Examples

```python
>>> is_obtuse(30, 60) # other angle is 90 so right triangle
False
>>> is_obtuse(100, 40) # has an angle 100, so obtuse
True
>>> is_obtuse(30, 30) # other angle is 120, so obtuse
True
>>> is_obtuse(60, 45) # other angle is 75, so acute
False
```
