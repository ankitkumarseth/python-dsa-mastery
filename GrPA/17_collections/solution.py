def reverse_first_half(t: tuple) -> tuple:
    '''
    Given an even-length tuple, return a new tuple where the first half 
    is reversed, and the second half remains unchanged.

    Arguments:
    t: tuple - an even-length tuple.

    Return: tuple - a new tuple with the first half reversed.
    '''
    mid = len(t) // 2
    return t[:mid][::-1] + t[mid:]

def delete_first_three(l: list) -> None:
    '''
    Given a list, delete the first three elements in the list.

    Arguments:
    l: list - a list of elements.

    Return: None - the list is modified in place.
    '''
    # for _ in range(3):
    #     l.pop(0) if l else None
    del l[:3]

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

def final_position(pos: tuple, vel: tuple, time:int) -> tuple:
    '''
    Given an initial position of a point moving in a cartesian plane with a constant velocity, 
    find the the final position of the point after a given time. 
    
    Hint: final position = intial position + velocity * time

    Args:
        pos - tuple[int]: A tuple representing the position vector (x1, y1).
        vel - tuple[int]: A tuple representing the velocity vector (vx, vy).
        time - int: time of movement.

    Returns:
        tuple[int]: A tuple representing the displacement (dx, dy).
    '''
    x1, y1 = pos
    vx, vy = vel
    dx, dy = x1 + vx*time, y1 + vy*time
    return dx, dy
