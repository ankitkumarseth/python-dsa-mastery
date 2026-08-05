# NOTE: Do NOT use a `for` loop anywhere in this file.

task = input()

if task == "sum_until_0":
    """
    Example Input:
    5
    3
    2
    0
    Expected Output:
    10
    """
    sum = 0
    while (num:= int(input())) != 0:
        sum += num
    print(sum)
    
    # --- Pythonic Alternative (Sentinel Iterator) ---
    # print(sum(iter(lambda: int(input()), 0)))

elif task == "total_price":
    """
    Example Input:
    2 50
    1 100
    END
    Expected Output:
    200
    """
    total = 0
    while (user_input:= input()) != "END":
        qty, price = user_input.split()
        total += int(qty) * int(price)
    print(total)
    
    # --- Pythonic Alternative (Generator Expression & Sentinel) ---
    # print(sum(int(qty) * int(price) for line in iter(input, "END") for qty, price in [line.split()]))

elif task == "only_ed_or_ing":
    """
    Example Input:
    Reading
    start
    STOP
    Expected Output:
    Reading
    """
    while (word:= input()) != "STOP":
        if word.lower().endswith(("ed", "ing")):
            print(word)

elif task == "reverse_sum_palindrome":
    """
    Example Input:
    56
    -1
    Expected Output:
    56
    """
    while (num:= int(input())) != -1:
        total = num + int(str(num)[::-1])
        total_str = str(total)
        if total_str == total_str[::-1]:
            print(num)

elif task == "double_string":
    """
    Example Input:
    hello

    Expected Output:
    hellohello
    """
    while (string:= input()) != "":
        print(string * 2)

elif task == "odd_char":
    """
    Example Input:
    Hello
    WORLD.
    Expected Output:
    Hlo WRD
    """
    words = []
    while True:
        word = input()
        words.append(word[::2])
        if word.endswith("."):
            break
    print(" ".join(words))


elif task == "only_even_squares":
    """
    Example Input:
    3
    4
    NAN
    Expected Output:
    16
    """
    while (num_str:= input()) != 'NAN':
        num = int(num_str)
        if num % 2 == 0:
            print(num ** 2)

elif task == "only_odd_lines":
    """
    Example Input:
    one
    two
    three
    END
    Expected Output:
    three
    one
    """
    lines = []
    while (line:= input()) != 'END':
        lines.append(line)
    result = "\n".join(lines[::2][::-1])
    print(result)

