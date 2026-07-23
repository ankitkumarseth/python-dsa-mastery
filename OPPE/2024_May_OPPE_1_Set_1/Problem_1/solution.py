def abs_diff_between_sum_and_sum_of_squares(a:int, b:int) -> int:
    '''
    Given two integers, find the absolute difference between
    their sum and the sum of their squares.
    Eg.
    a, b = 2,3
    sum is 5
    sum of squares is 13
    absolute difference is 8
    '''
    ...

def swap_except_middle_three(s: str) -> str:
    '''
    Given an odd-length string,
    swap the parts before and after the middle three characters,
    while keeping the middle three characters in place.

    Assume the string has at least 5 characters.

    Examples:
        "firstabclast1" -> "last1abcfirst"
        "abcdefghi" -> "ghidefabc"
    '''
    ...

def interleave_lists(list1, list2, list3):
    '''
    Given three lists of same length,
    interleave them together and return the interleaved list.

    Example:
        list1 = [1, 2, 3]
        list2 = ['a', 'b', 'c']
        list3 = [(1,1),(2,2),(3,3)]
        output = [1, 'a', (1,1), 2, 'b', (2,2), 3, 'c', (3,3)]
    '''
    ...

def has_more_than_5_unique_digits(num: int) -> bool:
    '''
    Determine if a given integer has more than 5 unique digits.
    '''
    ...

def final_position(pos: tuple, vel: tuple, time:int) -> tuple:
    '''
    Given an initial position of a point moving in a cartesian plane with a constant velocity,
    find the the final position of the point after a given time.

    Hint: final position = intial position + velocity * time
    '''
    ...

def remove_keys_not_in_list(d: dict, l: list) -> None:
    '''
    Remove keys from a dictionary that are not present in a given list.
    The function modifies the dictionary in place and does not return anything.

    Note:
        Modifying a dict while iterating over it will give an error in python.
        So, make a copy of the dict keys and then iterate over it.
    '''
    ...
