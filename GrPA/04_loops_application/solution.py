any = None
all = None
min = None
task = input()
if task == 'factors':
    '\n    Find the factors of a number n (including 1 and itself) in ascending order.\n    Example Input:\n    28\n    Expected Output:\n    1\n    2\n    4\n    7\n    14\n    28\n    '
    pass
elif task == 'find_min':
    '\n    Take n numbers from the input and print the minimum number.\n    Example Input:\n    5\n    10\n    20\n    5\n    25\n    15\n    Expected Output:\n    5\n    '
    pass
elif task == 'prime_check':
    '\n    Check whether a given number is prime or not.\n    Example Input:\n    17\n    Expected Output:\n    True\n    '
    pass
elif task == 'is_sorted':
    '\n    Check if all characters of the given string from input are in alphabetical order. Print the output as "True" or "False" accordingly.\n    Example Input:\n    abcdefg\n    Expected Output:\n    True\n    '
    pass
elif task == 'any_true':
    '\n    Take n numbers from input and check if any of the numbers are divisible by 3. Print the output as "True" or "False" accordingly.\n    Example Input:\n    4\n    10\n    15\n    20\n    25\n    Expected Output:\n    True\n    '
    pass
elif task == 'manhattan':
    '\n    Take inputs directions such as "UP", "DOWN", "LEFT" and "RIGHT" from the input until the input is "STOP". Assume you are starting from (0,0) in a cartesian coordinate. Find the Manhattan distance between the starting point and the ending point by following the steps in the cartesian plane.\n    Example Input:\n    UP\n    UP\n    LEFT\n    DOWN\n    RIGHT\n    RIGHT\n    STOP\n    Expected Output:\n    2\n    '
    pass
else:
    print('Invalid Task')
