import math

def get_angle(x,y):
    return math.atan2(y,x)

def process_points(points:set, task:str):
    """Process the ponts according to the given task.

    Args:
        points (set[tuple[int,int]]) - Set of points in 
            cartesian corrdinates as (x,y) tuples
        task (str) - String with one of the below values.
            - 'sort_close_to_y_axis'
            - 'closest_point_to_origin'
            - 'group_by_quadrant'

    Returns:
        The output of the corresponding task.

    """
    ...
