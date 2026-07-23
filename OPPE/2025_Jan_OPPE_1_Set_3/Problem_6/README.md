# Analyze Sentences

Write a function `process_sentence(sentence, task)` that analyzes a given sentence and computes the following according the task specified:

- `count_words` - Total number of words in the sentence.
- `count_palindromes` - Total number of palindrome words.
- `count_words_with_repeated_chars` - Total number of words that contain at least one repeated character.
- `words_with_max_len` - A set of longest words in the sentence (by number of characters).

Assume words are separated by spaces.

**NOTE:** This is a function type question, you don't have to take input or print the output, just have to complete the required function definition. You can define helper functions if needed, but the actual solution should be in the given function template.

### Examples

**1. count_words**
```python
>>> sentence = "level noon civic radar something"
>>> process_sentence(sentence,"count_words")
5
```

**2. count_palindromes**
```python
>>> sentence = "level noon civic radar something"
>>> process_sentence(sentence, "count_palindromes")
4
```

**3. count_words_with_chars_repeated**
```python
>>> sentence = "hello world programming fun and interesting"
>>> process_sentence(sentence,"count_words_with_repeated_chars")
3
```

**4. words_with_max_len**
```python
>>> sentence = "hello world programming fun and interesting"
>>> process_sentence(sentence, "words_with_max_len")
{'interesting', 'programming'}
```
