def reverse(L: list) -> list:
    '''
    Write a recursive function named reverse that accepts a list L as argument 
    and returns the reversed list.

    Args:
        L (list): A list of elements.

    Returns:
        list: The reversed list.
    '''
    if not L:
        return L
    return [L[-1]] + reverse(L[:-1])

def linear(P: list, Q: list, k: int) -> bool:
    '''
    Write a recursive function named linear that accepts two lists P and Q, 
    and an integer k. It should return True only if both conditions are satisfied:
    1. P and Q are of the same length.
    2. P[i] = k * Q[i], for every integer i in the range [0, len(P)-1].

    Args:
        P (list): A non-empty list of positive integers.
        Q (list): A non-empty list of positive integers.
        k (int): A positive integer.

    Returns:
        bool: True if the conditions are satisfied, else False.
    '''
    if len(P) != len(Q):
        return False
    if not P:
        return True
    return P[0] == k * Q[0] and linear(P[1:], Q[1:], k)

def collatz(n: int) -> int:
    '''
    The Collatz function is defined for a positive integer n as follows:
    f(n) = 3n + 1 if n is odd
    f(n) = n / 2 if n is even

    Write a recursive function named collatz that accepts a positive integer n 
    and returns the number of times f has to be applied repeatedly in order 
    to first reach 1.

    Args:
        n (int): A positive integer (1 < n <= 32,000).

    Returns:
        int: The number of times f(n) has to be applied to reach 1.
    '''
    if n == 1:
        return 0
    if n % 2 == 0:
        return collatz(n // 2) + 1
    else:
        return collatz(3* n + 1) + 1

def steps(n: int) -> int:
    '''
    Fibonacci likes to climb steps either 1 at a time, 2 at a time, or 3 at a time.
    Write a recursive function named steps that accepts a positive integer n as argument. 
    It should return the total number of ways in which Fibonacci can ascend n steps.

    Args:
        n (int): The total number of steps to climb.

    Returns:
        int: The total number of ways to climb the steps.
    '''
    if n < 0:
        return 0
    if n == 0:
        return 1
    return steps(n - 1) + steps(n - 2) + steps(n - 3)


def ancestry(P: dict, present: str, past: str) -> list:
    '''
    Given a dictionary P of father-son relationships (key=son, value=father),
    return the sequence of ancestors of the person named 'present', traced 
    all the way back up to the person named 'past'.

    Args:
        P (dict): A dictionary mapping son to father.
        present (str): The name of the starting person.
        past (str): The name of the ancestor to trace back to.

    Returns:
        list: A sequence of ancestors from present to past.
    '''
    if present  == past:
        return [past]
    return [present] + ancestry(P, P.get(present), past)
