# GrPA Nested Loops

Create a multi-functional program that performs different tasks based on the user input. The program should support the following tasks:

### Tasks

* **`permutation`**: Given a string `s`, print all the possible two-letter permutations (without repetition of the same index) of the letters in the string.
### Examples
**Input:**
```text
permutation
abc
```
**Output:**
```text
ab
ac
ba
bc
ca
cb
```

* **`sorted_permutation`**: Given a string `s`, print all the possible two-letter permutations (without repetition) of the letters in the string where the first character comes before the second one in alphabetical order. The order in which the permutations are printed is the same as the previous one (Type: Filtering).
### Examples
**Input:**
```text
sorted_permutation
bca
```
**Output:**
```text
bc
ab
ac
```

* **`repeat_the_repeat`**: Given a number `n`, print the numbers from 1 to `n` in the same line and repeat this `n` times.
### Examples
**Input:**
```text
repeat_the_repeat
3
```
**Output:**
```text
123
123
123
```

* **`repeat_incrementally`**: Given a number `n`, print a pattern where the `k`-th line contains the first `k` numbers and there are `n` lines in total. 
### Examples
**Input:**
```text
repeat_incrementally
4
```
**Output:**
```text
1
12
123
1234
```

* **`increment_and_decrement`**: Given a number `n`, print a pattern where the `k`-th line should have the numbers from 1 to `k` and then back down to 1. 
### Examples
**Input:**
```text
increment_and_decrement
3
```
**Output:**
```text
1
121
12321
```
