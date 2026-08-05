any = None
all = None
min = None
task = input()
if task == 'factors':
    '\n    Find the factors of a number n (including 1 and itself) in ascending order.\n    Example Input:\n    28\n    Expected Output:\n    1\n    2\n    4\n    7\n    14\n    28\n    '
    n = int(input())
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
elif task == 'find_min':
    '\n    Take n numbers from the input and print the minimum number.\n    Example Input:\n    5\n    10\n    20\n    5\n    25\n    15\n    Expected Output:\n    5\n    '
    n = int(input())
    minimum = int(input())
    for _ in range(n - 1):
        val = int(input())
        if val < minimum:
            minimum = val
    print(minimum)
elif task == 'prime_check':
    '\n    Check whether a given number is prime or not.\n    Example Input:\n    17\n    Expected Output:\n    True\n    '
    n = int(input())
    if n <= 1:
        print(False)
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print(False)
                break
        else:
            print(True)
elif task == 'is_sorted':
    '\n    Check if all characters of the given string from input are in alphabetical order. Print the output as "True" or "False" accordingly.\n    Example Input:\n    abcdefg\n    Expected Output:\n    True\n    '
    s = input()
    is_sorted = True
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            is_sorted = False
            break
    print(is_sorted)
elif task == 'any_true':
    '\n    Take n numbers from input and check if any of the numbers are divisible by 3. Print the output as "True" or "False" accordingly.\n    Example Input:\n    4\n    10\n    15\n    20\n    25\n    Expected Output:\n    True\n    '
    n = int(input())
    result = False
    for i in range(n):
        num = int(input())
        if num % 3 == 0:
            result = True
            break
    print(result)
elif task == 'manhattan':
    '\n    Take inputs directions such as "UP", "DOWN", "LEFT" and "RIGHT" from the input until the input is "STOP". Assume you are starting from (0,0) in a cartesian coordinate. Find the Manhattan distance between the starting point and the ending point by following the steps in the cartesian plane.\n    Example Input:\n    UP\n    UP\n    LEFT\n    DOWN\n    RIGHT\n    RIGHT\n    STOP\n    Expected Output:\n    2\n    '
    x, y = (0, 0)
    while (user_input := input()) != 'STOP':
        if user_input == 'RIGHT':
            x += 1
        elif user_input == 'LEFT':
            x -= 1
        elif user_input == 'UP':
            y += 1
        elif user_input == 'DOWN':
            y -= 1
    print(abs(x - 0) + abs(y - 0))
else:
    print('Invalid Task')