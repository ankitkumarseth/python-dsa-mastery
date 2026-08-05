task = input()
if task == 'sum_until_0':
    '\n    Example Input:\n    5\n    3\n    2\n    0\n    Expected Output:\n    10\n    '
    sum = 0
    while (num := int(input())) != 0:
        sum += num
    print(sum)
elif task == 'total_price':
    '\n    Example Input:\n    2 50\n    1 100\n    END\n    Expected Output:\n    200\n    '
    total = 0
    while (user_input := input()) != 'END':
        qty, price = user_input.split()
        total += int(qty) * int(price)
    print(total)
elif task == 'only_ed_or_ing':
    '\n    Example Input:\n    Reading\n    start\n    STOP\n    Expected Output:\n    Reading\n    '
    while (word := input()) != 'STOP':
        if word.lower().endswith(('ed', 'ing')):
            print(word)
elif task == 'reverse_sum_palindrome':
    '\n    Example Input:\n    56\n    -1\n    Expected Output:\n    56\n    '
    while (num := int(input())) != -1:
        total = num + int(str(num)[::-1])
        total_str = str(total)
        if total_str == total_str[::-1]:
            print(num)
elif task == 'double_string':
    '\n    Example Input:\n    hello\n\n    Expected Output:\n    hellohello\n    '
    while (string := input()) != '':
        print(string * 2)
elif task == 'odd_char':
    '\n    Example Input:\n    Hello\n    WORLD.\n    Expected Output:\n    Hlo WRD\n    '
    words = []
    while True:
        word = input()
        words.append(word[::2])
        if word.endswith('.'):
            break
    print(' '.join(words))
elif task == 'only_even_squares':
    '\n    Example Input:\n    3\n    4\n    NAN\n    Expected Output:\n    16\n    '
    while (num_str := input()) != 'NAN':
        num = int(num_str)
        if num % 2 == 0:
            print(num ** 2)
elif task == 'only_odd_lines':
    '\n    Example Input:\n    one\n    two\n    three\n    END\n    Expected Output:\n    three\n    one\n    '
    lines = []
    while (line := input()) != 'END':
        lines.append(line)
    result = '\n'.join(lines[::2][::-1])
    print(result)