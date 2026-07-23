# Check if a Number is Divisible by Exactly One of the Given Numbers

Write a function `div_by_exactly_one` that takes three integers `num`, `a`, and `b`. The function should return `True` if `num` is divisible by exactly one of the numbers `a` or `b`, and `False` otherwise.

**NOTE:** This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

### Examples

**Input:**
```
num=20, a=5, b=6
```
**Output:**
```
True
```
*(20 is divisible by 5 only)*

**Input:**
```
num=20, a=5, b=10
```
**Output:**
```
False
```
*(20 is divisible by both 5 and 10)*

**Input:**
```
num=20, a=6, b=10
```
**Output:**
```
True
```
*(20 is divisible by 10 only)*

**Input:**
```
num=20, a=6, b=7
```
**Output:**
```
False
```
*(20 is not divisible by either 6 or 7)*
