# Count Strings with Length Divisible by Either 3 or 5

Write a function `count_strings_length_divisible_by_3_or_5(strings)` that takes a list of strings and counts how many strings have lengths divisible by either 3 or 5.

### Examples
```python
strings = [
    "misunderstanding", "inconsiderately", 
    "characters", "computers"
]
print(count_strings_length_divisible_by_3_or_5(strings)) # Output: 3
```

**Explanation:**
- "misunderstanding" has 16 characters which is not divisible by either 3 or 5. Thus not counted.
- "inconsiderately" has 15 characters which is divisible by both 3 and 5. Thus counted.
- "characters" has 10 characters which is divisible by 5. Thus counted.
- "computers" has 9 characters which is divisible by 3. Thus counted.
