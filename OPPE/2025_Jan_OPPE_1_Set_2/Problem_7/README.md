# Pattern Printing - Z Pattern

You are tasked with drawing a Z-shaped pattern using asterisks (`*`). The Z pattern is a right-angled triangle with horizontal lines at the top and bottom, and a diagonal line from the top-right to the bottom-left.

Note that there should be no space after the last `*` in a line.

### Input Format
A single integer `n` representing the size of the Z pattern (i.e., the number of rows and columns). It is guaranteed that `n >= 3`.

### Output Format
Print the Z pattern with `n` rows, each containing `n` characters (either a `*` or a space). The pattern should be drawn with:
- A row of asterisks at the top.
- A diagonal line of asterisks from the top-right to the bottom-left.
- A row of asterisks at the bottom.

### Examples

**Input 1:**
```
3
```
**Output 1:**
```
***
 *
***
```

**Input 2:**
```
5
```
**Output 2:**
```
*****
   *
  *
 *
*****
```

**Input 3:**
```
4
```
**Output 3:**
```
****
  *
 *
****
```
