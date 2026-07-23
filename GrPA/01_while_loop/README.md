# GrPA While Loop - Multi-functional Program

### ✅ Important Note on `while` loops 🔁:
* Use `while` only when the number of iterations is indefinite.
* If you can term the steps as "do n times", "do once for each item", etc. use a `for` loop instead.
* If you can only term the steps as "do until something happens" (e.g. when a user inputs 10), use a `while` loop.

> [!IMPORTANT]
> **NOTE:** None of this problem statement can be written using a `for` loop since the number of repetitions is indefinite.

## Problem Statement

Problem type: Standard Input - Standard Output

Implement different parts of a multi-functional program based on an initial input value. Each part of the program will handle various tasks related to accumulation, filtering, mapping, and combinations of these operations. None of the tasks should use explicit loops for definite repetitions, and the program should handle indefinite inputs gracefully.

### Tasks

**Accumulation - Accumulating a final result**
* `sum_until_0`: Continuously read integers from standard input until you receive a `0`. Print the sum of these integers.
### Examples
**Input:**
```text
sum_until_0
5
3
2
0
```
**Output:**
```text
10
```

* `total_price`: Continuously read pairs of integers from standard input, representing the quantity and price of items, until you receive the string `"END"`. Print the total price of all items.
### Examples
**Input:**
```text
total_price
2 50
1 100
END
```
**Output:**
```text
200
```

**Filtering - Selecting based on a criterion**
* `only_ed_or_ing`: Continuously read strings from standard input until you encounter the word `"STOP"` (case insensitive and not included in the output). Print only those strings that end with `"ed"` or `"ing"` (case insensitive).
### Examples
**Input:**
```text
only_ed_or_ing
Reading
start
STOP
```
**Output:**
```text
Reading
```

* `reverse_sum_palindrome`: Continuously read positive integers from standard input until you encounter a `"-1"` (not included in the output). Print only those integers for which the sum of the number and its reverse is a palindrome.
### Examples
**Input:**
```text
reverse_sum_palindrome
56
-1
```
**Output:**
```text
56
```

**Mapping - Applying the same operation to different items**
* `double_string`: Continuously read lines from standard input until an empty line is encountered. Print each line repeated twice.
### Examples
**Input:**
```text
double_string
hello

```
**Output:**
```text
hellohello
```

* `odd_char`: Continuously read strings from standard input until you encounter a string ending with a `"."` (include that string with the `.` in the output). Extract characters at odd positions (starting from 1) of each line, and print the results in a single line separated by spaces.
### Examples
**Input:**
```text
odd_char
Hello
WORLD.
```
**Output:**
```text
Hlo WRD
```

**Filter and Map - Applying an operation to selected items**
* `only_even_squares`: Continuously read numbers from standard input until `"NAN"` is encountered. Print the square of each number only if it is even.
### Examples
**Input:**
```text
only_even_squares
3
4
NAN
```
**Output:**
```text
16
```

**Filter and Accumulate - Accumulating a result with selected items**
* `only_odd_lines`: Continuously read lines from standard input until `"END"` (not included in the output) is encountered. Create a string by prepending only the odd lines (starting from 1) with a newline character in between, and print the result which will be the odd lines in reverse order.
### Examples
**Input:**
```text
only_odd_lines
one
two
three
END
```
**Output:**
```text
three
one
```
