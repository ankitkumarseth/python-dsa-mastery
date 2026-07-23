# Reorder the Jumbled Lines

Given a text file with several lines followed by a single line containing a comma-separated list of integers, reorder the lines of the text file based on the given order and print them.

- The integers in the last line specify the new order of the preceding lines.
- Each number corresponds to the position of a line (1-based index) in the original text.
- Maintain the exact formatting and order as specified in the last line separated by comma.

**NOTE:** This is a file-in-stdout type question where the input is read from the file and the output is printed in the standard output.

### Examples

**Input:**
```
first line 
second line 
third line
fourth line
3,4,2,1
```
*(Note: example formatting adjusted to match actual TCs comma-separated integer style)*
**Output:**
```
third line
fourth line
second line
first line
```

**Input:**
```
2. Explicit is better than implicit.
4. Complex is better than complicated.
1. Beautiful is better than ugly.
5. Flat is better than nested.
3. Simple is better than complex.
3,1,5,2,4
```
**Output:**
```
1. Beautiful is better than ugly.
2. Explicit is better than implicit.
3. Simple is better than complex.
4. Complex is better than complicated.
5. Flat is better than nested.
```
