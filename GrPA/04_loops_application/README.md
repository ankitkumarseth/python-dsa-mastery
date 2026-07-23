# GrPA Loop Application

You are tasked with writing a program that can handle various tasks based on the input. The first line of the input represents the task to be performed. 

*(Note: To ensure that you cannot use the built in `any`, `all` and `min` function for this exercise, they have been disabled in the template code. You must implement the logic manually.)*

### Tasks

* **`factors`**: Find the factors of a number `n` (including 1 and itself) in ascending order.
### Examples
**Input:**
```text
factors
28
```
**Output:**
```text
1
2
4
7
14
28
```

* **`find_min`**: Take `n` numbers from the input and print the minimum number.
### Examples
**Input:**
```text
find_min
5
10
20
5
25
15
```
**Output:**
```text
5
```

* **`prime_check`**: Check whether a given number is prime or not.
### Examples
**Input:**
```text
prime_check
17
```
**Output:**
```text
True
```

* **`is_sorted`**: Check if all characters of the given string from input are in alphabetical order. Print the output as `"True"` or `"False"` accordingly.
### Examples
**Input:**
```text
is_sorted
abcdefg
```
**Output:**
```text
True
```

* **`any_true`**: Take `n` numbers from input and check if any of the numbers are divisible by 3. Print the output as `"True"` or `"False"` accordingly.
### Examples
**Input:**
```text
any_true
4
10
15
20
25
```
**Output:**
```text
True
```

* **`manhattan`**: Take inputs directions such as `"UP"`, `"DOWN"`, `"LEFT"` and `"RIGHT"` from the input until the input is `"STOP"`. Assume you are starting from (0,0) in a cartesian coordinate. Find the Manhattan distance between the starting point and the ending point by following the steps in the cartesian plane.
### Examples
**Input:**
```text
manhattan
UP
UP
LEFT
DOWN
RIGHT
RIGHT
STOP
```
**Output:**
```text
2
```
