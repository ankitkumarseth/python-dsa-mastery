def format_as_second_comma_first(tup: tuple) -> str:
    '''
    Format Elements in tuple as "second, first"
    Given a tuple of length two create a string in the format of "second, first" where first and second are the first and second elements in the tuple.

    The elements can be of any data type.

    Example:
    >>> format_as_second_comma_first(('hello', 'python'))
    'python, hello'
    >>> format_as_second_comma_first((1, 2))
    '2, 1'
    >>> format_as_second_comma_first((1.2, 3.4))
    '3.4, 1.2'
    '''
    ...


def even_first_odd_reversed(s: str) -> str:
    '''
    Return a string with the characters in the even indices first
    and the characters in the odd indices reversed next.

    Arguments:
    s: str - the input string

    Return:
    str - modified string

    Example:
    >>> even_first_odd_reversed('abcde')
    'acedb'
    >>> even_first_odd_reversed('python')
    'ptonhy'
    >>> even_first_odd_reversed('abracadabra')
    'arcdbaraaab'
    '''
    ...


def is_palindrome(n: int) -> bool:
    '''
    Checks if an integer is a palindrome.

    Arguments:
    n: int - the integer to check

    Return:
    bool - True if the integer is a palindrome, False otherwise

    Example:
    >>> is_palindrome(121)
    True
    >>> is_palindrome(123)
    False
    >>> is_palindrome(-121)
    False
    '''
    ...
