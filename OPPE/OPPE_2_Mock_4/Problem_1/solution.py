def second_largest(lst: list) -> int:
    '''
    Given a list of integers, return the second largest number in the list.
    Consider that list contains at least two integers.

    Arguments:
    lst: list - the input list of integers

    Return:
    int - the second largest number in the list

    Example:
    >>> second_largest([1, 2, 3, 4, 5])
    4
    '''
    pass

def arithmetic_operations(t: tuple) -> tuple:
    '''
    Given a tuple of two integers (a, b), return a tuple containing the 
    sum, difference, product, and quotient (integer division) of the two numbers.

    Arguments:
    t: tuple - a tuple of two integers (a, b)

    Return:
    tuple - a tuple containing the sum, difference, product, and quotient

    Example:
    >>> arithmetic_operations((1, 2))
    (3, -1, 2, 0)
    '''
    pass

def not_present_in_both(lst1: list, lst2: list) -> list:
    '''
    Given two lists, return a list containing the items 
    that are present in either list 1 or list 2 but not in both.

    Arguments:
    lst1: list - the first list 
    lst2: list - the second list 

    Return:
    set - a set containing the items present in either list 1 or list 2 but not in both

    Example:
    >>> symmetric_difference([1, 2, 3], [3, 4, 5])
    {1, 2, 4, 5}
    '''
    pass

def modify_string_1(s: str) -> str:
    '''
    Given a string, Seperate the characters present in odd and even indices
    and return the merged string with even indices first and odd indices second in reverse order.

    Arguments:
    s: str - the input string

    Return:
    str - modified string

    Example:
    >>> modify_string_1('abcde')
    'acedb'
    >>> modify_string_1('python')
    'ptonhy'
    '''
    pass

def create_count_dict(lst1: list, lst2: list) -> dict:
    '''
    Given two lists, lst1 and lst2, return a dictionary where each item 
    of lst1 is the key and the corresponding value is the count of that 
    item in lst2.

    Arguments:
    lst1: list - the first list of items to be used as keys
    lst2: list - the second list of items from which to count occurrences

    Return:
    dict - a dictionary with items from lst1 as keys and their counts in lst2 as values

    Example:
    >>> create_count_dict(['a', 'b', 'c'], ['a', 'b', 'a', 'a', 'c', 'c', 'c'])
    {'a': 3, 'b': 1, 'c': 3}
    '''
    pass

def average_of_numbers(lst: list) -> float:
    '''
    Given a list containing integers, floats, and strings, return the average 
    of the integers and floats, rounded to two decimal points. If neither 
    integers nor floats are present, return -1.

    Arguments:
    lst: list - a list containing integers, floats, and strings

    Return:
    float - the average of the integers and floats rounded to two decimal points,
            or -1 if no integers or floats are present

    Example:
    >>> average_of_numbers([1, 2.5, 'a', 3, 'b'])
    2.17
    >>> average_of_numbers(['a', 'b', 'c'])
    -1
    '''
    pass
