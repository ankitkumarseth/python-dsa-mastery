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
    s = input()
    for i in range(len(s)):
        for j in range(len(s)):
            if i != j:
                print(s[i] + s[j])
                
    # --- Pythonic Alternative (Itertools) ---
    # [print("".join(p)) for p in permutations(s, 2)]

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
    s = input()
    for i in range(len(s)):
        for j in range(len(s)):
            if i != j and s[i] < s[j]:
                print(s[i] + s[j])
                
    # --- Pythonic Alternative (Itertools + Filter) ---
    # [print(a + b) for a, b in permutations(s, 2) if a < b]

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
    n = int(input())
    for i in range(1, n + 1):
        row = ''
        for j in range(1, n + 1):
            row += str(j)
        print(row)
        
    # --- Pythonic Alternative (Map & Generator Unpacking) ---
    # row = "".join(map(str, range(1, n + 1)))
    # print(*(row for _ in range(n)), sep='\n')

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
    n = int(input())
    for i in range(1, n + 1):
        row = ''
        for j in range(1, i+1):
            row += str(j)
        print(row)
        
    # --- Pythonic Alternative (Map & Generator Unpacking) ---
    # print(*("".join(map(str, range(1, i + 1))) for i in range(1, n + 1)), sep='\n')

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
    n = int(input())
    for i in range(1, n + 1):
        row = ''
        for j in range(1, i + 1):
            row += str(j)
        print(row + row[-2::-1])
        
    # --- Pythonic Alternative (Walrus Operator & Generator) ---
    # print(*( (r := "".join(map(str, range(1, i + 1)))) + r[-2::-1] for i in range(1, n + 1) ), sep='\n')

else:
    print("Invalid Task")
