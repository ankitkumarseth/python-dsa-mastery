from itertools import permutations
task = input()
if task == 'permutation':
    '\n    Given a string s, print all the possible two-letter permutations(without repitition) of the letters in the string.\n    Example Input:\n    abc\n    Expected Output:\n    ab\n    ac\n    ba\n    bc\n    ca\n    cb\n    '
    s = input()
    for i in range(len(s)):
        for j in range(len(s)):
            if i != j:
                print(s[i] + s[j])
elif task == 'sorted_permutation':
    '\n    Given a string s, print all the possible two-letter permutations(without repetition) of the letters in the string where the first character comes before the second one in alphabetical order.\n    Example Input:\n    bca\n    Expected Output:\n    bc\n    ab\n    ac\n    '
    s = input()
    for i in range(len(s)):
        for j in range(len(s)):
            if i != j and s[i] < s[j]:
                print(s[i] + s[j])
elif task == 'repeat_the_repeat':
    '\n    Given a number n, print the numbers from 1 to n in the same line and repeat this n times.\n    Example Input:\n    3\n    Expected Output:\n    123\n    123\n    123\n    '
    n = int(input())
    for i in range(1, n + 1):
        row = ''
        for j in range(1, n + 1):
            row += str(j)
        print(row)
elif task == 'repeat_incrementally':
    '\n    Given a number n, print a pattern where the k-th line contains the first k numbers and there are n lines in total.\n    Example Input:\n    4\n    Expected Output:\n    1\n    12\n    123\n    1234\n    '
    n = int(input())
    for i in range(1, n + 1):
        row = ''
        for j in range(1, i + 1):
            row += str(j)
        print(row)
elif task == 'increment_and_decrement':
    '\n    Given a number n, print a pattern where the k-th line should have the numbers from 1 to k and then back down to 1.\n    Example Input:\n    3\n    Expected Output:\n    1\n    121\n    12321\n    '
    n = int(input())
    for i in range(1, n + 1):
        row = ''
        for j in range(1, i + 1):
            row += str(j)
        print(row + row[-2::-1])
else:
    print('Invalid Task')