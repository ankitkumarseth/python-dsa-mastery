# Simple Stemmer

Given a multiline text file containing lowercase words separated by spaces or newlines, stem each word (remove certain suffixes) according to the list of suffixes given in the `suffixes` list and print the contents in the same format.

Do not change the line or order of the words.

```python
suffixes = [
    'wards', 'ations', 'ation', 'tions', 'tion', 'asions', 
    'asion', 'sions', 'sion', 'ment', 'ness', 'ship', 
    'hood', 'able', 'ible', 'less', 'ward', 'wise', 'ion', 'ity', 'age',
    'ize', 'ise', 'ify', 'ate', 'ful', 'ous', 'ish', 'ive', 'ing', 'ers', 'er',
    'or', 'ty', 'en', 'ic', 'al', 'ly'
]
```

Remove the first suffix from the list of suffixes that matches a given word. For example for the word "education" the suffix "ation" and "tion" matches but "ation" is present first in the suffixes list thus the word is stemmed as "educ".

NOTE: This is a file-in-stdout type question where the input is read from the file and the output is printed in the standard output.

### Examples

**Input File (`test_input.txt`):**
```text
running faster stronger
organization management
happiness joyfulness sadness
```

**Output:**
```text
runn fast strong
organiz manage
happi joyful sad
```
