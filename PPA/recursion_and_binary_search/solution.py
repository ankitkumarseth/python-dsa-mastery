def triangular(n: int) -> int:
    '''
    Write a recursive function named triangular that accepts a positive integer n 
    as argument and returns the sum of the first n positive integers.
    '''
    pass

def factorial(n: int) -> int:
    '''
    Write a recursive function named factorial that accepts a positive integer n 
    as argument and returns the factorial of n.
    '''
    pass

def multiply(a: int, b: int) -> int:
    '''
    Write a recursive function named multiply that accepts two positive integers 
    a and b as argument and returns their product. You can only use + and - operators. 
    You are not allowed to use the * symbol anywhere in your code!
    '''
    pass

def logarithm(x: int) -> int:
    '''
    Write a recursive function named logarithm that accepts a positive integer x 
    (which is a power of 2) as argument and returns log2(x).
    '''
    pass

def palindrome(word: str) -> bool:
    '''
    Write a recursive function named palindrome that accepts a string word as argument 
    and returns True if it is a palindrome and False otherwise.
    '''
    pass

def spiral_iterative(left: int, right: int, n: int) -> float:
    '''
    An iterative function to compute the x-coordinate of the nth arm of the spiral.
    
    Parameters:
        left: integer - x-coordinate of the point P_0
        right: integer - x-coordinate of the point P_1
        n: integer - the number of arms in the spiral
    Return:
        result: float - the x-coordinate of P_n
    '''
    pass

def spiral_recursive(left: int, right: int, n: int) -> float:
    '''
    A recursive function to compute the x-coordinate of the nth arm of the spiral.
    
    Arguments:
        left: integer - x-coordinate of the point P_0
        right: integer - x-coordinate of the point P_1
        n: integer - the number of arms in the spiral
    Return:
        result: float - the x-coordinate of P_n
    '''
    pass

def count(L: list, word: str) -> int:
    '''
    Write a recursive function named count that accepts a list of words L and a word.
    This function should return the number of occurrences of word in L.
    You cannot use the built-in count method for lists.
    '''
    pass

def non_decreasing(L: list) -> bool:
    '''
    Write a recursive function named non_decreasing that accepts a non-empty list L 
    of integers as argument and returns True if the elements are sorted in 
    non-decreasing order from left to right, and False otherwise.
    '''
    pass

def uniq(L: list) -> list:
    '''
    Write a recursive function named uniq that accepts a non-empty list L as argument 
    and returns a new list after removing all duplicates from it. Your function must 
    retain the last occurrence of each distinct element in the list.
    '''
    pass

def search(L: list, k: int) -> bool:
    '''
    Write a recursive function named search that accepts a sorted list of integers L 
    and an integer k. The function should return True if k is found in the list L, 
    and False otherwise.
    '''
    pass

def insert(L: list, x: int) -> list:
    '''
    Write a function named insert that accepts a sorted list L of integers and an 
    integer x as arguments. It should return a sorted list with the element x inserted 
    into the input list at the right place.
    '''
    pass

def isort(L: list) -> list:
    '''
    Write a recursive function named isort that accepts a non-empty list L of integers 
    as argument. It should return a sorted list in ascending order. 
    isort must make use of insert.
    '''
    pass

def poly(L: list, x_0: float) -> float:
    '''
    Write a recursive function named poly that accepts the list of coefficients L 
    and a real number x_0 as arguments. It should return the polynomial evaluated 
    at the value x_0.
    '''
    pass

def power(A: list, m: int) -> list:
    '''
    Write a recursive function named power that accepts a square matrix A 
    and a positive integer m as arguments and returns A^m.
    '''
    pass

def subset_sum(L: list, s: int) -> bool:
    '''
    Write a recursive function named subset_sum that accepts a list of positive 
    integers L and a positive integer s as arguments. Return True if you can withdraw 
    some subset of coins whose combined worth is s, return False otherwise.
    '''
    pass
