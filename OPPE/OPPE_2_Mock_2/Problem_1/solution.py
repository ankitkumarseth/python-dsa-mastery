def percentage_increase(original, new):
    '''Calculate the percentage increase from the original value to the new value.

    Args:
        original (float): The original value.
        new (float): The new value.

    Returns:
        float: The percentage increase.

    Examples:
    >>> percentage_increase(50, 75)
    50.0
    >>> percentage_increase(80, 100)
    25.0
    '''
    pass

def is_ten_digit_even(n):
    '''Returns True if the number is a 10 digit even number, False otherwise.

    Args: 
        n (int): The given number. 

    Returns: 
        bool : result as True or False. 

    >>> is_ten_digit_even(8769473839)
    False
    >>> is_ten_digit_even(9289479278)
    True
    '''
    pass

def find_indices_of_element(l, elem):
    '''Find all indices of an element in a list.

    Args:
        l (list): The input list.
        elem: The element to find.

    Returns:
        list: A list of indices where the element is found.

    Examples:
    >>> find_indices_of_element([1, 2, 3, 2, 4], 2)
    [1, 3]
    >>> find_indices_of_element(['a', 'b', 'a', 'c'], 'a')
    [0, 2]
    '''
    pass

def swap_adjacent_elements(t):
    '''Swap every pair of adjacent elements in the tuple.

    Args:
        t (tuple): A tuple of even length.

    Returns:
        tuple: A new tuple with adjacent elements swapped.

    Examples:
    >>> swap_adjacent_elements((1, 2, 3, 4, 5, 6))
    (2, 1, 4, 3, 6, 5)
    >>> swap_adjacent_elements(('a', 'b', 'c', 'd'))
    ('b', 'a', 'd', 'c')
    '''
    pass

def common_chars(word1, word2): 
    '''Find all the unique common charecters present in the given words
    and return them as a string in ascending order.

    Arg:
        word1 (str) : Input string. 
        word2 (str) : Input string. 

    Returns: 
        str: string of unique common charecters arranged in ascending order. 

    >>> common_chars('apple', 'ball')
    'al'
    >>> common_chars('abcde', 'edfci')
    'cde'
    '''
    pass

def count_values_occurrences(d):
    '''Count the number of occurrences of each value in the dictionary.

    Args:
        d (dict): The input dictionary.

    Returns:
        dict: A dictionary where the keys are the values from the input dictionary, 
        and the values are their occurrence counts.

    Examples:
    >>> count_values_occurrences({'a': 1, 'b': 2, 'c': 1})
    {1: 2, 2: 1}
    >>> count_values_occurrences({1: 'x', 2: 'y', 3: 'x'})
    {'x': 2, 'y': 1}
    '''
    pass
