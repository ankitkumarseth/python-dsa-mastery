def squares_of_odds(lst: list) -> list:
    '''
    Given a list of integers, return a list containing the squares of all the odd integers in the input list.

    Arguments:
    lst: list - a list of integers

    Return:
    list - a list containing the squares of all the odd integers in the input list

    Example:
    >>> squares_of_odds([1, 2, 3, 4, 5])
    [1, 9, 25]
    >>> squares_of_odds([2, 4, 6])
    []
    '''
    pass

def pair_elements(t1: tuple, t2: tuple) -> tuple:
    '''
    Given two tuples of equal length, create a new tuple where each element
    is a pair from the corresponding elements of the input tuples.

    Arguments:
    t1: tuple - the first tuple
    t2: tuple - the second tuple of the same length as t1

    Return:
    tuple - a new tuple where each element is a pair from the corresponding
            elements of the input tuples

    Example:
    >>> pair_elements((1, 2, 3), ('a', 'b', 'c'))
    ((1, 'a'), (2, 'b'), (3, 'c'))
    >>> pair_elements((4, 5), (6, 7))
    ((4, 6), (5, 7))
    '''
    pass

def modify_string_2(t: tuple) -> str:
    '''
    Given a tuple containing two elements, return a formatted string "Last, First".

    Arguments:
    t: tuple - a tuple two elements -> First, Last

    Return:
    str - a formatted string "Last, First"

    Example:
    >>> modify_string_2(('hello', 'python'))
    python, hello
    '''
    pass

def unique_vowels(s: str) -> set:
    '''
    Given a string, return a set of unique vowels present in the string.

    Arguments:
    s: str - the input string

    Return:
    set - a set of unique vowels present in the string

    Example:
    >>> unique_vowels('aeiou')
    {'u', 'i', 'o', 'e', 'a'}
    '''
    pass

def invert_dictionary(input_dict):
    """
    Inverts a dictionary so that the keys become values and the values become keys.

    Arguments:
        input_dict (dict): The dictionary to invert.

    Returns:
        dict: The inverted dictionary.

    Example:
    >>> invert_dictionary({'a': 1, 'b': 2, 'c': 3})
    {1: 'a', 2: 'b', 3: 'c'}
    """
    pass

def factorial(n: int) -> float:
    '''
    Find the factorial of the given number
    Note: Factorial of 0 is 1

    Arguments:
    n: integer 

    Return:
    int - factorial of the given number

    Example:
    >>> factorial(5)
    120
    >>> factorial(-5)
    -120
    '''
    pass
