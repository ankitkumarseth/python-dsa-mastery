# Uppercase Every k-th Vowel and lower case other vowels in a File

Write a program that uppercases every k-th vowel in a text file and lowercases other vowels. Vowels are `a, e, i, o, u` and the check should be case-insensitive. The case of consonants should be unchanged.

Assume `k` is a positive integer.

- The first line of the file contains the integer `k`.
- Subsequent lines of the file contain the text.
- The vowel count is cumulative across the entire text. For example, if `k=3`, the 3rd, 6th, 9th, etc., vowels found in the file should be uppercased, regardless of which line they are on.

NOTE: This is a file-in-stdout type question where the input is read from the file and the output is printed in the standard output.

### Examples

**Input(contents of the file):**
```text
3
This is a sample text.
it has many vowels.
every third one becomes uppercase.
```

**Output:**
```text
This is A sample tExt.
it has mAny vowels.
Every third One becOmes uppErcase.
```
