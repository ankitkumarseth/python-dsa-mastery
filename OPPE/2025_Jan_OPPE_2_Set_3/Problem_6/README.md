# Polygon Analysis

Given a list of points representing the vertices of a polygon in anti-clockwise direction, implement various functions to analyze the properties of the polygon.

- **perimeter**: The total length of the polygon, calculated by summing the distances between consecutive vertices. Given the vertices $p1,p2,...,pn$, the perimeter is given by `dist(p1,p2) + dist(p2,p3) + ... + dist(pn, p1)`
- **bounding_box**: The smallest rectangle that can contain the polygon, represented by the coordinates of its bottom-left and top-right corners. Given the vertices as `(x1,y1), (x2,y2), ... ,(xn,yn)`, the bottom-left coordinate is given by `(min(x1,x2...,xn), min(y1,y2,...,yn))` and the top-right coordinate is given by `(max(x1,x2,...,xn), max(y1,y2,...,yn))`.
- **area**: The area of the polygon using the Shoelace formula, based on the coordinates of the vertices. Area of a polygon = Half the sum of determinants of coordinates of adjacent vertices (in anti-clockwise order) = `1/2*(det([p1,p2]) + det([p2,p3]) + ... + det([pn,p1]))`.
- **is_convex**: A check to determine if the polygon is convex. A polygon is convex if the z component of the cross product is greater than or equal to zero for all the vector pairs formed by consecutive edges (in anti-clockwise direction), i.e, `zcross(p[i],p[i+1],p[i+2]) > 0` for all adjacent edges `((p[i],p[i+1]),(p[i+1],p[i+2]))`

The helper functions `det_2x2`, `distance`, and `zcross` given in the template can be utilized.

### Example
```python
points = [(2,1),(5,1),(7,3),(4,6),(1,4)]

perimeter = distance((2,1),(5,1)) + ... + distance((4,6),(1,4)) + distance((1,4),(2,1))
          = 3 + 2.83 + 4.24 + 3.61 + 3.16 = 16.84

minimum values in x and y coordinates are 1 and 1 respectively
maximum values in x and y coordinates are 7 and 6 respectively
Thus, bounding_box = ((1,1),(7,6))

area  = 1/2* (det([(2,1),(5,1)])+...+det([(1,4),(2,1)]))
      = 1/2 *(-3 + 8 + 30 + 10 + -7)
      = 38/2 = 19

zcross values are:
    zcross((2,1),(5,1),(7,3)) = 6 
    zcross((5,1),(7,3),(4,6)) = 12
    zcross((7,3),(4,6),(1,4)) = 15
    zcross((4,6),(1,4),(2,1)) = 11
    zcross((1,4),(2,1),(5,1)) = 9

All values are positive thus convex.
```
