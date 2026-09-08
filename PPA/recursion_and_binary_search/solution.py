def triangular(n: int) -> int:
    '''
    Write a recursive function named triangular that accepts a positive integer n 
    as argument and returns the sum of the first n positive integers.
    '''
    return  n + triangular(n-1) if n > 0 else 0

def factorial(n: int) -> int:
    '''
    Write a recursive function named factorial that accepts a positive integer n 
    as argument and returns the factorial of n.
    '''
    return n * factorial(n-1) if n > 0 else 1

def multiply(a: int, b: int) -> int:
    '''
    Write a recursive function named multiply that accepts two positive integers 
    a and b as argument and returns their product. You can only use + and - operators. 
    You are not allowed to use the * symbol anywhere in your code!
    '''
    return a + multiply(a, b-1) if b > 0 else 0

def logarithm(x: int) -> int:
    '''
    Write a recursive function named logarithm that accepts a positive integer x 
    (which is a power of 2) as argument and returns log2(x).
    '''
    if x == 1:
        return 0
    return 1 + logarithm(x // 2)

def palindrome(word: str) -> bool:
    '''
    Write a recursive function named palindrome that accepts a string word as argument 
    and returns True if it is a palindrome and False otherwise.
    '''
    if len(word) <= 1:
        return True
    return palindrome(word[1:-1]) if word[0] == word[-1] else False

def spiral_iterative(left: float, right: float, n: int) -> float:
    '''
    An iterative function to compute the x-coordinate of the nth arm of the spiral.
    
    Parameters:
        left: integer - x-coordinate of the point P_0
        right: integer - x-coordinate of the point P_1
        n: integer - the number of arms in the spiral
    Return:
        result: float - the x-coordinate of P_n
    '''
    if n == 1:
        return right
    for _ in range(n-1):
        avg = (left + right) / 2
        left = right
        right = avg
    return right

def spiral_recursive(left: float, right: float, n: int) -> float:
    '''
    A recursive function to compute the x-coordinate of the nth arm of the spiral.
    
    Arguments:
        left: integer - x-coordinate of the point P_0
        right: integer - x-coordinate of the point P_1
        n: integer - the number of arms in the spiral
    Return:
        result: float - the x-coordinate of P_n
    '''
    if n == 1:
        return right
    avg = (left + right) / 2
    return spiral_recursive(right, avg, n - 1)

def count(L: list, word: str) -> int:
    '''
    Write a recursive function named count that accepts a list of words L and a word.
    This function should return the number of occurrences of word in L.
    You cannot use the built-in count method for lists.
    '''
    if not L:
        return 0
    return (1 if L[0] == word else 0) + count(L[1:], word)

def non_decreasing(L: list) -> bool:
    '''
    Write a recursive function named non_decreasing that accepts a non-empty list L 
    of integers as argument and returns True if the elements are sorted in 
    non-decreasing order from left to right, and False otherwise.
    '''
    if len(L) < 2:
        return True
    return non_decreasing(L[1:]) if L[0] <= L[1] else False

def uniq(L: list) -> list:
    '''
    Write a recursive function named uniq that accepts a non-empty list L as argument 
    and returns a new list after removing all duplicates from it. Your function must 
    retain the last occurrence of each distinct element in the list.
    '''
    if len(L) < 2:
        return L
    if L.count(L[0]) == 1:
        return [L[0]] + uniq(L[1:])
    else:
        return uniq(L[1:])

def search(L: list, k: int) -> bool:
    '''
    Write a recursive function named search that accepts a sorted list of integers L 
    and an integer k. The function should return True if k is found in the list L, 
    and False otherwise.
    '''
    if len(L) == 0:
        return False
    mid = len(L) // 2
    if L[mid] == k:
        return True
    elif k < L[mid]:
        return search(L[:mid], k)
    else:
        return search(L[mid+1:], k)

def insert(L: list, x: int) -> list:
    '''
    Write a function named insert that accepts a sorted list L of integers and an 
    integer x as arguments. It should return a sorted list with the element x inserted 
    into the input list at the right place.
    '''
    if not L:
        return [x]
    if x < L[0]:
        return [x] + L

    return [L[0]] + insert(L[1:], x)


def isort(L: list) -> list:
    '''
    Write a recursive function named isort that accepts a non-empty list L of integers 
    as argument. It should return a sorted list in ascending order. 
    isort must make use of insert.
    '''
    if len(L) < 2:
        return L
    return insert(isort(L[1:]), L[0])

def poly(L: list, x_0: float) -> float:
    '''
    Write a recursive function named poly that accepts the list of coefficients L 
    and a real number x_0 as arguments. It should return the polynomial evaluated 
    at the value x_0.
    '''
    if len(L) == 0:
        return 0
    return L[0] + poly(L[1:], x_0) * x_0

def multiply_matrix(mat1, mat2) -> list:
    n = len(mat1)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

def power(A: list, m: int) -> list:
    '''
    Write a recursive function named power that accepts a square matrix A 
    and a positive integer m as arguments and returns A^m.
    '''
    if m == 1:
        return A
    return multiply_matrix(A, power(A, m-1))

def subset_sum(L: list, s: int) -> bool:
    '''
    Write a recursive function named subset_sum that accepts a list of positive 
    integers L and a positive integer s as arguments. Return True if you can withdraw 
    some subset of coins whose combined worth is s, return False otherwise.
    '''
    if s == 0:
        return True
    elif s < 0:
        return False
    elif s > 0 and not L:
        return False

    return subset_sum(L[1:], s-L[0]) or subset_sum(L[1:], s)
