# Count Words with Matching First/Last but Different Second/Second-Last Letters

Write a function `count_special(words)` that receives a list of words (strings) and returns the number of words that satisfy both of the following conditions (the check is case-insensitive):
1. The first and the last characters of the word are the same.
2. The second character and the second-last character of the word are different.

Assume each word has at least two characters.

NOTE: This is a function type question. You do not need to read input or print output; just implement the function and return the required integer.

### Examples
- `count_special(["Bulb", "deed", "civic", "Noon", "lol"])` -> `1`
  - "Bulb": B == b (yes), u != l (yes) -> counted
  - "deed": d == d (yes), e != e (no) -> not counted
  - "civic": c == c (yes), i != i (no) -> not counted
  - "Noon": N == n (yes), o != o (no) -> not counted
- `count_special(["abca", "aXba", "xyzzyx", "abcaXab"])` -> `2`
  - "abca": a == a (yes), b != c (yes) -> counted
  - "aXba": a == a (yes), X != b (yes) -> counted
  - "xyzzyx": x == x (yes), y != y (no) -> not counted
  - "abcaXab": a == b (no) -> ignored
