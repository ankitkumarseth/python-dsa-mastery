# GrPA Lambda, Zip, Enumerate, Map, Filter

Implement the following functions according to the docstrings. This exercise tests your ability to use built-in functional programming tools like `map`, `filter`, `zip`, `enumerate`, and `lambda` functions.

> [!WARNING]
> **Note:** For specific functions, you are not allowed to use `if` statements, `for`/`while` loops, or comprehensions (like list/set/dict comprehensions). You must use `map`, `filter`, `lambda`, etc., instead!

### Functions to Implement

* **`is_greater_than_5(numbers: list) -> list`**: Given a list of numbers, return a list of bools corresponding to whether the number is greater than 5.
### Examples
**Input:**
```python
is_greater_than_5([3, 4, 5, 6, 7])
```
**Output:**
```text
[False, False, False, True, True]
```

* **`filter_less_than_5(numbers: list) -> list`**: Given a list of numbers, return a list of numbers that are less than 5.
### Examples
**Input:**
```python
filter_less_than_5([3, 4, 5, 6, 7])
```
**Output:**
```text
[3, 4]
```

* **`sum_of_two_digit_numbers(numbers: list)`**: Given a list of numbers find the sum of all two digit numbers.
### Examples
**Input:**
```python
sum_of_two_digit_numbers([8, 9, 10, 11, 12])
```
**Output:**
```text
33
```

* **`is_all_has_a(words: list) -> bool`**: Given a list of words check if all words has the letter a (case insensitive) in it.
### Examples
**Input:**
```python
is_all_has_a(["Apple", "Orange", "Banana"])
is_all_has_a(["Apple", "Orange", "Kiwi"])
```
**Output:**
```text
True
False
```

* **`print_with_numbering(items: list)`**: Print a list in multiple lines with numbering.
### Examples
**Input:**
```python
print_with_numbering(["Apple", "Orange", "Banana"])
```
**Output:**
```text
1. Apple
2. Orange
3. Banana
```

* **`parallel_print(countries: list, capitals: list)`**: Print the countries and capitals in multiple lines separated by a hyphen with space around it.
### Examples
**Input:**
```python
parallel_print(
  ["United States", "Brazil", "Nigeria", "India", "Australia"],
  ["Washington, D.C.", "Brasilia", "Abuja", "New Delhi", "Canberra"]
)
```
**Output:**
```text
United States - Washington, D.C.
Brazil - Brasilia
Nigeria - Abuja
India - New Delhi
Australia - Canberra
```

* **`make_dict(keys, values)`**: Create a dict with keys and values.
### Examples
**Input:**
```python
make_dict("abcd", [1, 2, 3, 4])
```
**Output:**
```text
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

* **`indices_of_big_words(words: list) -> list`**: Given a list of words, find the indices of the big words (length greater than 5).
### Examples
**Input:**
```python
indices_of_big_words(["Apple", "Banana", "Orange", "Kiwi", "Cherry"])
```
**Output:**
```text
[1, 2, 4]
```

* **`decode_rle(chars: str, repeats: list) -> str`**: Create a string with i-th char from chars repeated i-th value of repeats number of times. (Note: rle refers to Run-length encoding).
### Examples
**Input:**
```python
decode_rle("abcd", [2, 4, 3, 1])
```
**Output:**
```text
aabbbbcccd
```
