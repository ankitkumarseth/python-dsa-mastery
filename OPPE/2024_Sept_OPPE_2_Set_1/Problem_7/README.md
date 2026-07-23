# Ubbi Dubbi - Add "ub" and "dub" Alternately Before Vowels in the Text

Given a text file containing lowercase letters, modify the text such that:
- Before each vowel, add the string `"ub"` if it is the first or an odd-numbered vowel encountered.
- Add `"dub"` before the vowel if it is the second or an even-numbered vowel encountered.
- Preserve the text's original formatting, including spaces and newlines.

Assume the input text is all lowercase and may have multiple lines.

**NOTE:** This is a file-in-stdout type question where the input is read from the file and the output is printed in the standard output.

### Examples

**Input:**
```
hello world
python is good
```
**Output:**
```
hubelldubo wuborld
pythdubon ubis gduboubod
```
