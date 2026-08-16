# Thresholding a 2D Array and Printing with * and @

Given an `n x n` 2D array of integers (0 to 255) and a threshold `t`, replace each value with `@` if it is greater than or equal to `t`, otherwise replace it with `*`.

### Input Format
- The first line contains two integers: `n` (the number of rows of the image) and `t` (the threshold).
- The next `n` lines contain `n` integers (in the range 0-255) for the image.

### Output Format
Print the thresholded array, each element separated by spaces over multiple lines.
There should be no space in the beginning or the end of each line.

*Word of wisdom: This task is also known as thresholding in image processing. Usually image pixels are represented with values from 0-255.*

### Examples

**Input 1:**
```text
3 5
7 2 8
4 5 3
6 0 7
```
**Output 1:**
```text
@ * @
* @ *
@ * @ 
```

**Input 2:**
```text
2 50
10 70
60 40
```
**Output 2:**
```text
* @
@ *
```
