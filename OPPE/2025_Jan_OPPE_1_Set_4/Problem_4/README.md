# First Non-Repeating Character in a String

Write a function `first_non_repeating_char(s)` that returns the first non-repeating character in the string `s`. If no such character exists, return `None`.

### Example

```python
>>> s = "abcab" # c is the only non repeating char
>>> first_non_repeating_char(s)
'c'
>>> s = "aabbcc"
>>> first_non_repeating_char(s) # all chars are repeating
None
>>> s = "buzzingbee" # u, i, n and g are non repeating and first is "u"
>>> first_non_repeating_char(s)
'u'
```
