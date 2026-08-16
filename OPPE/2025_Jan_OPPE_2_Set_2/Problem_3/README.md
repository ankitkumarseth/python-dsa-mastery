# Check if both numbers have the same sign

Write a function `same_sign` that checks whether two given numbers have the same sign. Consider three cases:
1. Both numbers are strictly positive.
2. Both numbers are strictly negative.
3. Both numbers are zero.

The function should return `True` if the numbers have the same sign; otherwise, it should return `False`.

NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

### Examples
- `same_sign(10, 20)` -> `True` (Both numbers are strictly positive.)
- `same_sign(-5, -15)` -> `True` (Both numbers are strictly negative.)
- `same_sign(0, 0)` -> `True` (Both numbers are zero.)
- `same_sign(10, -20)` -> `False` (The numbers have different signs.)
- `same_sign(0, 10)` -> `False` (One number is zero, and the other is strictly positive.)
