# GrPA For Loop

### ✅ Important Note on `for` loops
In the context of general incremental definite loops, the structure of a `while` loop can be converted to a `for` loop using `range()`.

> [!WARNING]
> **NOTE:** The usage of `while` loops is strictly **NOT allowed** in this exercise! You must rewrite any provided `while` loops into `for` loops.

## Problem Statement

Write a multi-functional program that takes an input task from standard input and performs the corresponding task accordingly. 

### Part 1 - while loop to for loop
* **`factorial`**: Print the factorial of a given non-negative integer `n` (Type: Accumulation)
### Examples
**Input:**
```text
factorial
5
```
**Output:**
```text
120
```

* **`even_numbers`**: Print the even numbers from 0 (including) till the given input number `n` (including) in multiple lines (Type: Just Iterating)
### Examples
**Input:**
```text
even_numbers
5
```
**Output:**
```text
0
2
4
```

* **`power_sequence`**: Print the sequence 1, 2, 4, 8, 16, ... `n` terms in multiple lines, where `n` is taken from the input (Type: Mapping)
### Examples
**Input:**
```text
power_sequence
3
```
**Output:**
```text
1
2
4
```

### Part 2 - for loop With range
* **`sum_not_divisible`**: Print the sum of positive integers less than the given number `n` and not divisible by 4 and 5. (Type: Filtered Accumulation)
### Examples
**Input:**
```text
sum_not_divisible
10
```
**Output:**
```text
28
```

* **`from_k`**: Going in decreasing order starting from `k`, print the **reverse (digits reversed)** of the first `n` numbers which do not have the digit 5 and 9 and are odd numbers, in multiple lines.
### Examples
**Input:**
```text
from_k
3
55
```
**Output:**
```text
74
34
14
```

### Part 3 - for loop with iterables.
* **`string_iter`**: Given a string `s` of digits, print the numerical value of the digit multiplied by the previous digit. Assume the previous digit for the first element to be 1.
### Examples
**Input:**
```text
string_iter
1234
```
**Output:**
```text
1
2
6
12
```

* **`list_iter`**: Print the elements of a list `l` line by line in the format `{element} - type: {type}` where the element is the current element being iterated by the for loop and type is the type of the element.
### Examples
**Input:**
```text
list_iter
[1, "two"]
```
**Output:**
```text
1 - type: <class 'int'>
two - type: <class 'str'>
```
