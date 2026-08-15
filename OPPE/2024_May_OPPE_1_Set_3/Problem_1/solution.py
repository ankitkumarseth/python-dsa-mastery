def square_and_clip(x: int, threshold:int) -> int:
    '''
    Square the given integer and clip the result to threshold
    (clipping means if the value x goes greater than the threshold, keep it at threshold).

    Arguments:
    x: int - the input number
    threshold: int - the threshold value

    Return:
    int - squared and clipped result
    '''
    return min(x ** 2, threshold)

def lowercase_first_half_and_uppercase_second_half(s: str) -> str:
    '''
    Given an even-length string of any case, create a string with the first half
    in lowercase and the second half in uppercase.

    Arguments:
    s: str - the input string

    Return:
    str - the modified string
    '''
    mid = len(s) // 2
    return s[:mid].lower() + s[mid:].upper()

def add_the_middle_element_to_both_ends(l: list) -> None:
    '''
    Given an odd-length list, insert the middle element to both ends of the list.
    Modify the input list and do not return a new list.

    Arguments:
    l: list - the input list

    Return:
    None - the input list is modified inside the function.
    '''
    mid_value = l[len(l) // 2]
    l.insert(0, mid_value)
    l.append(mid_value)

def number_of_unique_common_digits(n1: int, n2: int) -> int:
    '''
    Given two integers, return the number of unique digits that are common in both numbers.
    Eg, 287498,295424 - 2, 4 and 9 are common to both nums so answer is 3
    Arguments:
    n1: int - the first number
    n2: int - the second number

    Return:
    int - the number of unique common digits.
    '''
    return len(set(str(n1)) & set(str(n2)))

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
    return abs(x1-x2) + abs(y1-y2) + abs(x2-x3) + abs(y2-y3)

def create_indexed_dict(names: list) -> dict:
    '''
    Given a list of names, create a dictionary with the indices as keys and the names as values.

    Args:
        names (list): A list of names.

    Returns:
        dict: A dictionary with indices as keys and names as values.
    '''
    return dict(enumerate(names))
    # return {key : name for key, name in enumerate(names)}
