# Count Vowels and Consonants in Even Indices

Given a string `s`, count the number of vowels and consonants that appear at even indices in the string (0-based indexing). Ignore non-alphabetical characters.

Implement the function `count_vowels_and_consonants_in_even_indices` that returns the counts as described above.

The string `s` can have both upper and lower case letters.

**NOTE:** This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

### Examples

**Input:**
```
"abcdeaeiou"
```
**Output:**
```
(4, 1)
```
*(Characters at even indices are: 'a', 'c', 'e', 'e', 'u'. Vowels: 'a', 'e', 'e', 'u' (4). Consonants: 'c' (1))*

**Input:**
```
"a11bc11de11"
```
**Output:**
```
(2, 1)
```
*(Characters at even indices are: 'a', '1', 'b', '1', 'd', '1'. Vowels: 'a' (1). Consonants: 'b', 'd' (2). Total wait: wait, example says vowels a, consonants b d... oh wait!
Ah, example says vowels (1), consonants (2)? No wait, in "a11bc11de11":
index 0: 'a' (vowel)
index 2: '1'
index 4: 'c' (consonant)
index 6: '1'
index 8: 'e' (vowel)
index 10: '1'
So 'a' and 'e' are vowels (2). 'c' is consonant (1). Yes, output is (2,1).)*

**Input:**
```
"ABCDE"
```
**Output:**
```
(2, 1)
```
*(Characters at even indices are: 'A', 'C', 'E'. Vowels: 'A', 'E' (2). Consonants: 'C' (1))*
