task = input()
if task == 'factorial':
    '\n    Example Input:\n    5\n    Expected Output:\n    120\n    '
    n = int(input())
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(result)
elif task == 'even_numbers':
    '\n    Example Input:\n    5\n    Expected Output:\n    0\n    2\n    4\n    '
    n = int(input())
    for i in range(0, n + 1, 2):
        print(i)
elif task == 'power_sequence':
    '\n    Example Input:\n    3\n    Expected Output:\n    1\n    2\n    4\n    '
    n = int(input())
    for i in range(n):
        print(2 ** i)
elif task == 'sum_not_divisible':
    '\n    Example Input:\n    10\n    Expected Output:\n    28\n    '
    n = int(input())
    total = 0
    for i in range(1, n):
        if i % 4 != 0 and i % 5 != 0:
            total += i
    print(total)
elif task == 'from_k':
    '\n    Example Input:\n    3\n    55\n    Expected Output:\n    74\n    34\n    14\n    '
    n = int(input())
    k = int(input())
    for i in range(k, -k, -1):
        if n == 0:
            break
        i_str = str(i)
        if i % 2 != 0 and '5' not in i_str and ('9' not in i_str):
            print(i_str[::-1])
            n -= 1
elif task == 'string_iter':
    '\n    Example Input:\n    1234\n    Expected Output:\n    1\n    2\n    6\n    12\n    '
    s = input()
    multiplier = 1
    for i in range(len(s)):
        if i != 0:
            multiplier = int(s[i - 1])
        print(int(s[i]) * multiplier)
elif task == 'list_iter':
    '\n    Example Input:\n    [1, "two"]\n    Expected Output:\n    1 - type: <class \'int\'>\n    two - type: <class \'str\'>\n    '
    lst = eval(input())
    for item in lst:
        print(f'{item} - type: {type(item)}')
else:
    print('Invalid')