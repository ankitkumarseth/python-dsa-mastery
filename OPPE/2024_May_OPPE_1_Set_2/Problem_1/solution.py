def is_right_triangle_with_even_sides(a:int,b:int,c:int) -> bool:
    '''
    Given three side lengths in the increasing
    order of length as a, b, and c, where a<=b<=c,
    check if the given sides are the sides of a right
    triangle whose perpendicular sides are of even length.

    Hint: in a right triangle the square of hypotenuse is the sum of square of other two sides.
    '''
    return a % 2 == 0 and b % 2 == 0 and a**2 + b**2 == c**2

def is_odd_indices_alpha_and_even_indices_digits(string: str) -> bool:
    '''
    Given a string, check if all the odd indices are alphabets and the even indices are digits.
    Note: indices starts from 0.
    '''
    return string[::2].isdigit() and string[1::2].isalpha()

def swap_even_and_odd_indices(l: list) -> None:
    '''
    Given a list of integers, swap the values at the even indices
    and the odd indices by modifying the same list.
    '''

    l[::2], l[1::2] = l[1::2], l[::2]
    # Alternate solution with for loop
    # for i in range(0, len(l), 2):
    #     l[i], l[i+1] = l[i+1], l[i]

def unique_chars_present_in_first_not_in_second(s1: str, s2: str) -> set:
    '''
    Given two words as strings, find the unique
    chars that are present in the first word but not in
    the second word.
    Assume all characters in the input are in lowercase.
    The order of elements in the set doesn't matter while returning.
    '''
    return set(s1) - set(s2)

def repeat(t: tuple) -> tuple:
    '''
    Given a tuple of length two, say (a,b), create a tuple
    with a repeated b number of times and b repeated a number of times.
    '''
    a, b = t
    return (a,) * b + (b,) * a

def num_squares(n: int) -> dict:
    '''
    Given an integer n, create a dictionary with the
    numbers from 1 to n (inclusive) as keys and their
    squares as values.
    '''
    return {i : i ** 2 for i in range(1, n + 1)}
