# String Rearrangement

Write a program that takes a text file with several lines. Each line has a string followed by indices separated by commas. The function should rearrange the characters in the string according to the given indices and print the updated strings.

- The indices specify the new order of characters in the string.
- Each number corresponds to the position (1-based index) in the original string.

NOTE: This is a file-in-stdout type question where the input is read from the file and the output is printed in the standard output.

### Examples

**Input File (`test_input.txt`):**
```text
hello,2,1,3,5,4
abcdef,3,2,1,6,5,4
xyz,3,1,2
```

**Output:**
```text
ehlol
cbafed
zxy
```
