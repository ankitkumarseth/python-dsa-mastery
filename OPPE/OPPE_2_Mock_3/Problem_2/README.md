# Happy Numbers

A happy number is a number defined by the following process:

1. Starting with any positive integer, replace the number by the sum of square of its digits.
2. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle that doesn't include 1.
3. Those numbers for which the process ends in 1 are happy.

### Example 1:
19 is a happy number.
Explanation:
- 1^2 + 9^2 = 82
- 8^2 + 2^2 = 68
- 6^2 + 8^2 = 100
- 1^2 + 0^2 + 0^2 = 1

### Example 2:
4 is not a happy number.
The cycle for 4 is as follows:
4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 (and repeats)

Define a function `n_happy_numbers` that accepts a list of positive integers and returns the count of happy numbers in the given list.
