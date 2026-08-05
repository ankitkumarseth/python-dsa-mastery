# NOTE: Do NOT use a `while` loop anywhere in this file.

task = input()

if task == 'factorial':
    """
    Example Input:
    5
    Expected Output:
    120
    """
    n = int(input())
    result = 1
    for i in range(2, n+1):
        result *= i
    print(result)
    
    # --- Pythonic Alternative ---
    # import math
    # print(math.factorial(n))

elif task == 'even_numbers':
    """
    Example Input:
    5
    Expected Output:
    0
    2
    4
    """
    n = int(input())
    for i in range(0, n+1, 2):
        print(i)
        
    # --- Pythonic Alternative (Unpacking) ---
    # print(*range(0, n+1, 2), sep='\n')

elif task == 'power_sequence':
    """
    Example Input:
    3
    Expected Output:
    1
    2
    4
    """
    n = int(input())
    for i in range(n): # similar to range (0,n)
        print(2 ** i)
        
    # --- Pythonic Alternative (Unpacking Generator) ---
    # print(*(2 ** i for i in range(n)), sep='\n')

elif task == 'sum_not_divisible':
    """
    Example Input:
    10
    Expected Output:
    28
    """
    n = int(input())
    total = 0
    for i in range(1, n):
        if i % 4 !=0 and i % 5 !=0:
            total += i
    print(total)
    
    # --- Pythonic Alternative (Generator inside sum()) ---
    # print(sum(i for i in range(1, n) if i % 4 != 0 and i % 5 != 0))

elif task == 'from_k':
    """
    Example Input:
    3
    55
    Expected Output:
    74
    34
    14
    """
    n = int(input())
    k = int(input())
    for i in range(k, -k, -1):
        if n == 0:
            break
        i_str = str(i)
        if i % 2 != 0 and '5' not in i_str and '9' not in i_str:
            print(i_str[::-1])
            n -= 1
            
    # --- Pythonic Alternative (Itertools & Generators) ---
    # import itertools
    # valid_nums = (str(i)[::-1] for i in itertools.count(k, -1) if i % 2 != 0 and not {'5', '9'} & set(str(i)))
    # print(*itertools.islice(valid_nums, n), sep='\n')

elif task == 'string_iter':
    """
    Example Input:
    1234
    Expected Output:
    1
    2
    6
    12
    """
    s = input()
    multiplier = 1
    for i in range(len(s)):
        if i != 0:
            multiplier = int(s[i-1])
        print(int(s[i]) * multiplier)
        
    # --- Pythonic Alternative (Sliding Window with Zip) ---
    # print(*(int(curr) * int(prev) for prev, curr in zip("1" + s, s)), sep='\n')

elif task == 'list_iter':
    """
    Example Input:
    [1, "two"]
    Expected Output:
    1 - type: <class 'int'>
    two - type: <class 'str'>
    """
    lst = eval(input())
    for item in lst:
        print(f"{item} - type: {type(item)}")
        
    # --- Pythonic Alternative (Safe Parsing) ---
    # import ast
    # [print(f"{item} - type: {type(item)}") for item in ast.literal_eval(input())]

else:
    print("Invalid")
