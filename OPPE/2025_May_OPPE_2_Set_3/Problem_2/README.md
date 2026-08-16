# Remove Second and Second-Last Character from String

Write a function `remove_second_and_second_last(s)` that receives a string `s` and returns a new string obtained after removing the second character (index 1) and the second-last character (index `len(s)-2`).

Assume the string will have atleast 4 characters.

NOTE: This is a function type question; you do not need to read input or print output, just implement the function.

### Examples
- `remove_second_and_second_last("abcdef")` -> `"acdf"` (remove 'b' at index 1 and 'e' at index 4)
- `remove_second_and_second_last("abcd")` -> `"ad"` (remove 'b' at index 1 and 'c' at index 2)
