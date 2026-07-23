# Number with More Unique Digits

Given two integers `n1` and `n2`, return the number that contains more unique digits.

If both numbers have the same number of unique digits, return the both as a tuple as `(n1, n2)`.

Assume both the integers `n1` and `n2` are positive integers.

*Hint: Use set to find the unique digits, as sets automatically eliminate duplicates.*

**NOTE:** This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

### Examples

**Input:**
```
n1 = 2345, n2 = 1111
```
**Output:**
```
2345
```
**Explanation:**
- `n1 = 2345` has the unique digits 2, 3, 4, 5 (4 unique digits).
- `n2 = 1111` has the unique digit 1 (1 unique digit).
- Since `n1` has more unique digits, the output is `2345`.

**Input:**
```
n1 = 1243, n2 = 123344
```
**Output:**
```
(1243, 123344)
```
**Explanation:**
- `n1 = 1243` has 4 unique digits.
- `n2 = 123344` has 4 unique digits.
- Since `n1` has the same number of unique digits, the output is `(1243, 123344)`.
