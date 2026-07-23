# Print Pattern - X

Given an integer `n` (where `n >= 0`), print an "X" shaped pattern with `n` rows above and below a central character `x`. The pattern should use backslashes (`\`) and forward slashes (`/`) to form the "X" shape, with increasing spaces between them as they approach the center. There should be no spaces to the right of the pattern.

**NOTE:** This is an I/O type question, you need to write the whole code for taking input and printing the output.

### Input Format
- A single integer `n`, representing the number of rows above and below the center of the "X".

### Output Format
- An "X" shaped pattern with `n` rows above and below a central `x` character, as described.

### Examples

**Input:**
```
0
```
**Output:**
```
x
```

**Input:**
```
1
```
**Output:**
```
\ /
 x
/ \
```

**Input:**
```
2
```
**Output:**
```
\   /
 \ /
  x
 / \
/   \
```
