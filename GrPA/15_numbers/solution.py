def seconds_to_minute_seconds(seconds: int) -> tuple:
    '''
    Given an integer representing seconds, return a tuple of (minutes, seconds).

    Arguments:
    seconds: int - an integer representing the number of seconds.

    Return: tuple - a tuple of (minutes, remaining_seconds).
    '''
    # return seconds // 60, seconds % 60
    return divmod(seconds, 60)

def create_indexed_dict(items: list) -> dict:
    '''
    Given a list of items, create a dictionary with the indices as keys and the items as items.

    Args:
        items (list): A list of items.

    Returns:
        dict: A dictionary with indices as keys and items as items.
    '''
    return dict(enumerate(items))

def manhattan_distance_via_b(a: tuple, b: tuple, c: tuple) -> int:
    '''
    Given three points a, b, and c on the Cartesian plane, 
    calculate the Manhattan distance to go from point a to point c via point b.

    Manhattan distance is the sum of the absolute differences of their Cartesian coordinates.

    Args:
        a (tuple): Coordinates of point a as (x1, y1).
        b (tuple): Coordinates of point b as (x2, y2).
        c (tuple): Coordinates of point c as (x3, y3).

    Returns:
        int: The Manhattan distance from point a to point c via point b.
    '''
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    return abs(x1 - x2) + abs(y1 - y2) + abs(x2 - x3) + abs(y2 - y3)

    pass

def is_right_triangle_with_even_sides(a:int,b:int,c:int) -> bool:
    '''
    Given three side lengths in the increasing 
    order of length as a, b, and c, where a<=b<=c,
    check if the given sides are the sides of a right 
    triangle whose perpendicular sides are of even length.

    Hint: in a right triangle the square of hypotenuse is the sum of square of other two sides.

    Arguments:
    a: int - the first side length
    b: int - the second side length
    c: int - the hypotenuse length

    Return:
    bool - True if the sides form a right triangle and the perpendicular sides are even, else False
    '''
    return a ** 2 + b ** 2 == c ** 2 and a % 2 == 0 and b % 2 == 0
