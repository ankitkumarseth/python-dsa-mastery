# this is to ensure that you cannot use the built in any, all and min function for this exercise but you can use it in the OPPEs.
any = None
all = None
min = None

task = input()

if task == 'factors':
    """
    Find the factors of a number n (including 1 and itself) in ascending order.
    Example Input:
    28
    Expected Output:
    1
    2
    4
    7
    14
    28
    """
    ...

elif task == 'find_min':
    """
    Take n numbers from the input and print the minimum number.
    Example Input:
    5
    10
    20
    5
    25
    15
    Expected Output:
    5
    """
    ...

elif task == 'prime_check':
    """
    Check whether a given number is prime or not.
    Example Input:
    17
    Expected Output:
    True
    """
    ...

elif task == 'is_sorted':
    """
    Check if all characters of the given string from input are in alphabetical order. Print the output as "True" or "False" accordingly.
    Example Input:
    abcdefg
    Expected Output:
    True
    """
    ...

elif task == 'any_true':
    """
    Take n numbers from input and check if any of the numbers are divisible by 3. Print the output as "True" or "False" accordingly.
    Example Input:
    4
    10
    15
    20
    25
    Expected Output:
    True
    """
    ...

elif task == 'manhattan':
    """
    Take inputs directions such as "UP", "DOWN", "LEFT" and "RIGHT" from the input until the input is "STOP". Assume you are starting from (0,0) in a cartesian coordinate. Find the Manhattan distance between the starting point and the ending point by following the steps in the cartesian plane.
    Example Input:
    UP
    UP
    LEFT
    DOWN
    RIGHT
    RIGHT
    STOP
    Expected Output:
    2
    """
    ...

else:
    print("Invalid Task")
