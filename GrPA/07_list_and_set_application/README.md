# GrPA List and Set Application

This exercise tests your ability to apply list and set operations to solve various problems.

### Functions to Implement

* **`find_min(items: list)`**: Find the minimum value in a list of integers.
### Examples
**Input:**
```python
find_min([1, 2, 3, 4, -4])
```
**Output:**
```text
-4
```

* **`odd_increment_even_decrement_no_modify(items: list) -> list`**: Increment all odd numbers by 1 and decrement all even numbers by 1, **without** modifying the original list.
### Examples
**Input:**
```python
odd_increment_even_decrement_no_modify([1, 2, 3, 4, 5, 6])
```
**Output:**
```text
[2, 1, 4, 3, 6, 5]
```

* **`odd_square_even_double_modify(items: list) -> list`**: Square all odd numbers and double all even numbers, modifying the input list **in place**.
### Examples
**Input:**
```python
odd_square_even_double_modify([1, 2, 3, 4, 5, 6])
```
**Output:**
```text
[1, 4, 9, 8, 25, 12]
```

* **`more_than_two_unique_vowels(sentence: str) -> set`**: Given a string of comma-separated words, return a set containing words that have more than two unique vowels.
### Examples
**Input:**
```python
more_than_two_unique_vowels("functions,are,not,complicated")
```
**Output:**
```text
{'complicated', 'functions'}
```

* **`sum_of_list_of_lists(lol: list) -> int`**: Find the sum of all integers in a list of lists.
### Examples
**Input:**
```python
sum_of_list_of_lists([
    [1, 2, 3, 4],
    [10, 20],
    [5],
])
```
**Output:**
```text
45
```

* **`flatten(lol: list) -> list`**: Flatten a list of lists into a single list.
### Examples
**Input:**
```python
flatten([
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]
])
```
**Output:**
```text
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
```

* **`all_common(strings: list) -> str`**: Find the characters that are common to all strings in a list and return them as a string in ascending order.
### Examples
**Input:**
```python
all_common([
    "abcde",
    "bcdef",
    "cdefg",
])
```
**Output:**
```text
cde
```

* **`vocabulary(sentences: list) -> set`**: Given a list of sentences (containing only alphabets and spaces), find the vocabulary (unique words). Convert all words to lowercase before adding them to the vocabulary.
### Examples
**Input:**
```python
vocabulary([
    "This is a car",
    "He is playing with a bat",
    "He and she are playing",
])
```
**Output:**
```text
{'a', 'and', 'are', 'bat', 'car', 'he', 'is', 'playing', 'she', 'this', 'with'}
```
