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
    n = int(input())
    
    # Standard Loop Approach
    for i in range(1, n + 1):
        if n % i  == 0:
            print(i)
            
    # Pythonic Alternative 1 (Generator Unpacking)
    # print(*(i for i in range(1, n + 1) if n % i == 0), sep='\n')
    
    # Pythonic Alternative 2 (String Join)
    # print('\n'.join(str(i) for i in range(1, n + 1) if n % i == 0))

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
    n = int(input())
    
    # Standard Loop Approach
    minimum = int(input())
    for _ in range(n-1):
        val = int(input())
        if val < minimum:
            minimum = val
    print(minimum)

    # Pythonic Alternative 1 (Sorting - O(N log N))
    # print(sorted(int(input()) for _ in range(n))[0])

    # Pythonic Alternative 2 (functools.reduce - O(N) and optimal)
    # from functools import reduce
    # print(reduce(lambda a, b: a if a < b else b, (int(input()) for _ in range(n))))

elif task == 'prime_check':
    """
    Check whether a given number is prime or not.
    Example Input:
    17
    Expected Output:
    True
    """
    n = int(input())
    if n <= 1:
        print(False)
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print(False)
                break
        else:
            # We only get here if the loop NEVER broke!
            print(True)

    # Pythonic Alternative 2 (Using all() - OPPE approved)
    # n = int(input())
    # print(False if n <= 1 else all(n % i != 0 for i in range(2, int(n**0.5) + 1)))

elif task == 'is_sorted':
    """
    Check if all characters of the given string from input are in alphabetical order. Print the output as "True" or "False" accordingly.
    Example Input:
    abcdefg
    Expected Output:
    True
    """

    # Loop Alternative (O(N) time complexity)
    s = input()
    is_sorted = True
    for i in range(len(s) - 1):
        if s[i] > s[i+1]:
            is_sorted = False
            break
    print(is_sorted)

    # Pythonic Alternative (O(N) using all and zip - OPPE approved)
    # s = input()
    # print(all(a <= b for a, b in zip(s, s[1:])))

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
    n = int(input())
    result = False
    for i in range(n):
        num = int(input())
        if num % 3 == 0:
            result = True
            break
    print(result)

    # Pythonic Alternative (Using any() with a generator - OPPE approved)
    # n = int(input())
    # print(any(int(input()) % 3 == 0 for _ in range(n)))

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
    x, y = 0, 0
    while (user_input := input()) != "STOP":
        if user_input == "RIGHT":
            x += 1
        elif user_input == "LEFT":
            x -= 1
        elif user_input == "UP":
            y += 1
        elif user_input == "DOWN":
            y -= 1
    print(abs(x-0) + abs(y-0))

    # Pythonic Alternative 1 (Using Match-Case - Python 3.10+)
    # x, y = 0, 0
    # while (direction := input()) != "STOP":
    #     match direction:
    #         case "RIGHT": x += 1
    #         case "LEFT":  x -= 1
    #         case "UP":    y += 1
    #         case "DOWN":  y -= 1
    # print(abs(x) + abs(y))

    # Pythonic Alternative 2 (Using Dictionary Mapping)
    # moves = {"RIGHT": (1, 0), "LEFT": (-1, 0), "UP": (0, 1), "DOWN": (0, -1)}
    # x, y = 0, 0
    # while (direction := input()) != "STOP":
    #     dx, dy = moves.get(direction, (0, 0))
    #     x += dx
    #     y += dy
    # print(abs(x) + abs(y))

else:
    print("Invalid Task")
