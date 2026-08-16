# GrPA 16 - Strings

This module covers 4 distinct problems focusing on string validation, slicing, and text processing.

## Check if odd indices are alphabets and even indices are digits
Given a string, check if all the odd indices are alphabets and the even indices are digits.
*Note: indices start from 0.*

### Example
**Input:**
```python
"a1b2c3"
```
**Output:**
```python
False
```
**Explanation:** Index 0 is an alphabet (`'a'`), but it should be a digit.

**Input:**
```python
"1a2b3c"
```
**Output:**
```python
True
```

## Check if an even-length string has A or a in the second half
Given an even-length string `s`, check if the second half contains the character `"a"` or `"A"`. Return `True` if it does, otherwise return `False`.

### Example
**Input:**
```python
"abcDef"
```
**Output:**
```python
False
```
**Explanation:** The second half is `"Def"`, which does not contain `"a"` or `"A"`, so the result is False.

## Most frequent first letter of a word in a multiline passage
Given a multi-line passage where the words are separated by spaces, find the letter which occurs most frequently as the first letter of any word. Consider both uppercase and lowercase letters as the same and return the letter in lowercase.
*Assume there will be only one letter that occurs the most number of times as the first letter of a word.*

### Example
**Input:**
```python
passage = '''
word1 Word2 word3 word4 text1 text2
text3 Text4 word5 text5 word6
python1 python2 Python3
'''
```
**Output:**
```python
'w'
```
**Explanation:** Words starting with 'w' or 'W' occur the most frequently in the passage.

## Remove First two and Last two Chars from a string
Given a string `s`, return a new string with the first two and last two characters removed.
If the string has less than four characters return an empty string.

### Example
**Input:**
```python
s = 'HelloWorld'
```
**Output:**
```python
'lloWor'
```
**Explanation:** Removing the first two ('He') and last two ('ld') characters results in 'lloWor'.
