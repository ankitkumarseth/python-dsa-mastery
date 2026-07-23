# Check if the Given String is Within Quotes and Has Quotes Inside

Write a function `within_and_has_double_quotes` that checks if a given string starts and ends with double quotes, and if there are double quotes inside the string (excluding the first and last characters). Return `True` if both conditions are met, and `False` otherwise.

**NOTE:** This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

### Examples

**Input:**
```
'"abcd"efgh"'
```
**Output:**
```
True
```
*(starts and ends with double quotes, and has double quotes inside)*

**Input:**
```
'abcd"efgh"'
```
**Output:**
```
False
```
*(does not start with double quotes)*

**Input:**
```
"'abcd'efgh'"
```
**Output:**
```
False
```
*(uses single quotes)*

**Input:**
```
'"abcdefgh"'
```
**Output:**
```
False
```
*(no double quotes inside the quotes)*
