# GrPA List Comprehension Exercises

These exercises will help you build the basics of list comprehensions.

> [!WARNING]
> **Note:** You cannot use `if` statements or loops (like standard `for` or `while` blocks) within the functions. You must use List Comprehensions!

### Tasks

* **`sum_of_squares(numbers: list)`**: Find the sum of the squares of all numbers in a list. (Concept: Mapping and aggregation)
### Examples
**Input:**
```python
sum_of_squares([1, 2, 3, 4])
```
**Output:**
```text
30
```

* **`total_cost(cart: list)`**: Given the quantity and price of each item as a list of tuples, find the total cost using list comprehensions.
### Examples
**Input:**
```python
total_cost([(1, 2), (3, 4), (1, 5)])
```
**Output:**
```text
19
```

* **`abbreviation(sentence: str)`**: Given a string containing multiple words separated by spaces, form an abbreviation by taking the first letter of each word and converting it to uppercase. (Concept: Mapping and aggregation)
### Examples
**Input:**
```python
abbreviation("ordinary wizarding levels")
```
**Output:**
```text
O.W.L.
```

* **`palindromes(words: list)`**: Given a list of strings, create a new list containing only the palindrome strings. (Concept: Filtering)
### Examples
**Input:**
```python
palindromes(["moon", "noon", "dad", "dog", "cat", "madam"])
```
**Output:**
```text
['noon', 'dad', 'madam']
```

* **`all_chars_from_big_words(sentence: str)`**: Find all unique characters (case-insensitive, convert all to lowercase) from words whose length is greater than 5 in a sentence. (Concept: Filtering)
### Examples
**Input:**
```python
all_chars_from_big_words("List comprehensions are a good start for functional programming")
```
**Output:**
```text
{'a', 'c', 'e', 'f', 'g', 'h', 'i', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u'}
```

* **`flatten(lol: list)`**: Flatten a nested list into a single list using list comprehension.
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

* **`unflatten(items: list, n_rows: int)`**: Given a flat list and the required number of rows, create a matrix (2D list) with that number of rows. (Concept: Nested aggregation)
### Examples
**Input:**
```python
unflatten([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4], 3)
```
**Output:**
```text
[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
```

* **`make_identity_matrix(m: int)`**: Create an identity matrix (ones on the main diagonal and zeros elsewhere) of the given size.
### Examples
**Input:**
```python
make_identity_matrix(3)
```
**Output:**
```text
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

* **`make_lower_triangular_matrix(m: int)`**: Given the number of rows m, create a lower triangular matrix as shown below.
### Examples
**Input:**
```python
make_lower_triangular_matrix(3)
```
**Output:**
```text
[[1, 0, 0], [1, 2, 0], [1, 2, 3]]
```
