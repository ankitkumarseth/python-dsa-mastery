# Cartesian Points Processing

Given a set of tuples of ints representing points in Cartesian coordinates, write a function that performs the following tasks:

- `sort_close_to_y_axis`: Returns a sorted list of the points based on the absolute value of their x-coordinate (distance from the y-axis). The point with the lower angle in polar coordinates comes first in case of ties.
- `closest_point_to_origin`: Find the closest point to the origin (0,0) based on the Manhattan distance. If there are multiple points at the same distance, return the one with the lower angle in polar coordinates.
- `group_by_quadrant`: Return a dictionary where the keys are quadrant numbers (1, 2, 3, 4) and the values are sets of points in those quadrants. Do not include keys for quadrants with no points.

Note the angle is computed using `math.atan2(y,x)` where `x` and `y` are the cartesian coordinates. `math.atan2` returns the angle in the range of -pi to pi. You can use the `get_angle` function from the template.

Assume no points are on the axes or origin and the coordinates are integers.

*Hint: `sorted` and `min` functions can be used with the key argument to make the code simpler.*

**Definitions:**
- Manhattan distance between two points `(x_1, y_1)` and `(x_2, y_2)` is `|x_1 - x_2| + |y_1 - y_2|`.

**NOTE:** This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

### Example

```python
points = {
    (2, 5), (-2, 6), (-2, 7), (-1, 3),
    (-3, -4), (4, -6), (0, 7)
}
task = "sort_close_to_y_axis"
```
**Output:**
```python
[
    (0, 7), (-1, 3), (2, 5), (-2, 7),
    (-2, 6), (-3, -4), (4, -6)
]
```
