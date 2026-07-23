# Get Next Roll Number

Write a function `next_roll_no` that takes a roll number `roll_no` as input and returns the next roll number in sequence within the same year and term.

The roll number format is `{yy}f{t}{num}`, where:
- `{yy}` represents the two-digit year
- `f` is a fixed character
- `{t}` represents the term number (1, 2, or 3)
- `{num}` is a six-digit number padded with zeros on the left

Assume the num part of the roll number will be less than 999999.

**NOTE:** This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

### Example

```python
next_roll_no("23f2000001") -> '23f2000002'
next_roll_no("24f3099999") -> '24f3100000'
```
