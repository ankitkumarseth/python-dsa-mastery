# Check Divisibility by Last Two Digits

Write a function that checks whether a given number is divisible by both of its last two digits.

Return `False` if any of the last two digits is zero.

**NOTE:** This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

### Input
A positive integer `num` with at least two digits.

### Output
`True` if the number is divisible by both of its last two digits, otherwise `False`.

### Examples

**Input:**
```
1236
```
**Output:**
```
True
```
*(1236 is divisible by both 3 and 6)*

**Input:**
```
345
```
**Output:**
```
False
```
*(345 is divisible by 5 but not divisible by 4)*

**Input:**
```
748
```
**Output:**
```
False
```
*(748 is divisible by 4 but not divisble by 8)*

**Input:**
```
740
```
**Output:**
```
False
```
*(the last digit is 0)*
