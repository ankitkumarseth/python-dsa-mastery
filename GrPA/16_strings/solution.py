from collections import Counter


def is_odd_indices_alpha_and_even_indices_digits(string: str) -> bool:
    '''
    Given a string, check if all the odd indices are alphabets and the even indices are digits.

    Note: indices starts from 0.

    Arguments:
    string: str - the input string

    Return:
    bool - True if all odd indices are alphabets and even indices are digits, else False
    '''
    return all(char.isdigit() for char in string[::2]) and all(char.isalpha() for char in string[1::2])

def has_a_in_second_half(s: str) -> bool:
    '''
    Given an even-length string, check if the second half contains 
    the character "a" or "A".

    Arguments:
    s: str - an even-length string.

    Return: bool - True if "a" or "A" is found in the second half, else False.
    '''
    mid = len(s) // 2
    return 'a' in s[mid:].lower()

def most_occuring_first_letter(passage: str) -> str:
    '''
    Returns the letter which occurs most frequently 
    as the first letter of any word.(case insensitive)

    Args:
        passage (str): A multi-line string representing the passage.

    Returns:
        str: The most frequently occurring first letter in lowercase.
    '''
    first_letters = [word[0].lower() for word in passage.split()]
    # return max(set(first_letters), key=first_letters.count)
    return Counter(first_letters).most_common(1)[0][0]

def remove_edges(s: str) -> str:
    '''
    Return a new string with the first two and last two 
    characters removed from the given string. 

    Arguments:
    s: str - a string.

    Return: str - a string with first and last two characters removed.
    '''
    return s[2:-2]
