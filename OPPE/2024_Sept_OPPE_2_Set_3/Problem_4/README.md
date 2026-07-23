# Get Words That Come After "the"

Write a function to find all the words that immediately follow the word "the" in a given sentence. The search should be case-insensitive, and words are separated by spaces.

**NOTE:** This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

### Examples

**Input:**
```
"The key and the lock is there"
```
**Output:**
```
['key', 'lock']
```
*("The" (case-insensitive) is followed by "key" and "the" is followed by "lock" hence, the output is ['key', 'lock'].)*

**Input:**
```
"The the and the The"
```
**Output:**
```
['the', 'and', 'The']
```
*("the" follows "The", "and" follows "the" and "The" follows "the".)*
