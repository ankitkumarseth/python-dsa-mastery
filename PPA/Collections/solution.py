from collections import deque
def rotate_list(lst: list, k: int) -> list:
    '''
    Given a list of items and an integer k, rotate the list to the right by k steps.

    Arguments:
    lst: list - a list of items
    k: int - the number of steps to rotate the list to the right

    Return:
    list - the rotated list

    Example:
    >>> rotate_list([1, 2, 3, 4, 5], 2)
    [4, 5, 1, 2, 3]
    >>> rotate_list(['a', 'b', 'c', 'd', 'e'], 3)
    ['c', 'd', 'e', 'a', 'b']
    '''

    k = (k % len(lst))
    return lst[-k:] + lst[:-k]

    # --- Pythonic Alternative (Optimized) ---
    # d = deque(lst)
    # d.rotate(k)
    # return list(d)

def swap_alternate_elements(t):
    '''
    Swap every alternate of adjacent elements in the tuple.

    Args:
        t (tuple): A tuple of even length.

    Returns:
        tuple: A new tuple with alternate elements swapped.

    Examples:
    >>> swap_alternate_elements((1, 2, 3, 4, 5, 6))
    (2, 1, 4, 3, 6, 5)
    >>> swap_alternate_elements(('a', 'b', 'c', 'd'))
    ('b', 'a', 'd', 'c')
    '''
    L = [None] * len(t)
    L[0::2] = t[1::2]
    L[1::2] = t[0::2]
    return tuple(L)

    # --- Pythonic Alternative (1-liner) ---
    # return tuple(x for pair in zip(t[1::2], t[0::2]) for x in pair)

def in_exactly_one(l1: list, l2: list) -> set:
    '''
    Given two lists, return a list containing the items
    that are present in either list but not in both.

    Arguments:
    l1: list - the first list
    l2: list - the second list

    Return:
    set - a set containing the items present in either list 1 or list 2 but not in both

    Example:
    >>> in_exactly_one([1, 2, 3], [3, 4, 5])
    {1, 2, 4, 5}
    '''
    return set(l1) ^ set(l2)

def unique_vowels(s: str) -> set:
    '''
    Given a string, return a set of unique vowels present in the string.

    Arguments:
    s: str - the input string

    Return:
    set - a set of unique vowels present in the string

    Examples:
    >>> unique_vowels('banana treat')
    {'a', 'e'}
    >>> unique_vowels('apple lolipop')
    {'a', 'e', 'i', 'o'}
    >>> unique_vowels('Ian Avinkov')
    {'I','A','a','i','o'}
    '''
    vowels = set('aeiouAEIOU')

    return vowels.intersection(s)
    
    # --- Pythonic Alternative (Set operator) ---
    # return vowels & set(s)


def common_char_sorted_str(s1:str, s2:str) -> str:
    '''
    Returns a sorted string with unique common charecters present in the given strings.

    Arg:
        s1 (str) : Input string.
        s2 (str) : Input string.

    Returns:
        str: string of unique common charecters arranged in ascending order.

    Examples:
    >>> common_char_sorted_str('apple', 'ball')
    'al'
    >>> common_char_sorted_str('abcde', 'edfci')
    'cde'
    '''
    return ''.join(sorted(set(s1) & set(s2)))
