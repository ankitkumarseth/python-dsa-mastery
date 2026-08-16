import math

def det_2x2(m) -> float:
    """Determinant of a 2x2 matrix."""
    a,b,c,d = *m[0], *m[1]
    return a*d - b*c

def distance(p1:tuple, p2:tuple) -> float:
    """Euclidean distance between two points."""
    x1, y1, x2, y2 = *p1, *p2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def zcross(A,B,C):
    """Z component of the cross product of the vectors formed by AB and BC.
    
    Args:
        A,B,C (tuple): Points A,B,C as (x,y) tuples.

    Returns:
        float: z component of the corss product.
    """
    ax, ay, bx, by, cx, cy = *A, *B, *C
    # computing vectors AB and BC by B-A and C-B
    ab,bc = (bx-ax, by-ay) , (cx-bx, cy-by)
    return det_2x2([ab,bc])

def perimeter(points: list) -> float:
    """Calculate the perimeter of the polygon.
    
    Args:
        points (list[tuple]): List of tuple representing the polygon in anti-clockwise order.

    Returns:
        float: the perimeter of the polygon.
    """
    pass
    
def bounding_box(points: list) -> tuple:
    """Calculate the bounding box of the polygon.
    
    Args:
        points (list[tuple]): List of tuple representing the polygon in anti-clockwise order.

    Returns:
        bottom_left (tuple), top_right (tuple): coordinates of the bottom left and top right vertices of the bounding box.
    """
    pass
    
def area(points: list):
    """Calculate the area of the polygon using the shoelace formula.
    
    Args:
        points (list[tuple]): List of tuple representing the polygon in anti-clockwise order.

    Returns:
        (int|float): the area of the polygon.
    """
    pass
    
def is_convex(points: list) -> bool:
    """Check if the polygon is convex using cross products.
    
    Args:
        points (list[tuple]): List of tuple representing the polygon in anti-clockwise order.

    Returns:
        (bool): True if the polygon is convex else concave.
    """
    pass
