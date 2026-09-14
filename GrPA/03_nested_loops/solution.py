from itertools import permutations

task = input()

if task == 'permutation':
    """
    Given a string s, print all the possible two-letter permutations(without repitition) of the letters in the string.
    Example Input:
    abc
    Expected Output:
    ab
    ac
    ba
    bc
    ca
    cb
    """
    pass
elif task == 'sorted_permutation':
    """
    Given a string s, print all the possible two-letter permutations(without repetition) of the letters in the string where the first character comes before the second one in alphabetical order.
    Example Input:
    bca
    Expected Output:
    bc
    ab
    ac
    """
    pass
elif task == 'repeat_the_repeat':
    """
    Given a number n, print the numbers from 1 to n in the same line and repeat this n times.
    Example Input:
    3
    Expected Output:
    123
    123
    123
    """
    pass
elif task == 'repeat_incrementally':
    """
    Given a number n, print a pattern where the k-th line contains the first k numbers and there are n lines in total.
    Example Input:
    4
    Expected Output:
    1
    12
    123
    1234
    """
    pass
elif task == 'increment_and_decrement':
    """
    Given a number n, print a pattern where the k-th line should have the numbers from 1 to k and then back down to 1.
    Example Input:
    3
    Expected Output:
    1
    121
    12321
    """
    pass
else:
    print('Invalid Task')
