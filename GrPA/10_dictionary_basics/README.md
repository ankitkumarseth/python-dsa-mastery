# Dictionary Operations

You are tasked with implementing a series of functions that perform various operations on dictionaries in Python. These functions will manipulate dictionaries that represent fruit prices and perform different operations as specified.

### `dictionary_operations(fruit_prices: dict, fruits: list)`
Perform a series of operations on the given `fruit_prices` dictionary based on the `fruits` list:
1. Add `fruits[0]` with a cost of 3.
2. Modify the cost of `fruits[1]` to 2.
3. Increase the cost of `fruits[2]` by 2.
4. Delete `fruits[3]` from `fruit_prices`.
5. Print the price of `fruits[4]`.
6. Print the names of fruits in `fruit_prices` as a sorted list.
7. Print the prices of fruits in `fruit_prices` as a sorted list.

*(Note: You are not allowed to use `if` statements or loops for this function).*

### Examples
**Input:**
```python
fruits = ["Apple", "Orange", "Grapes", "Banana", "Cherry"]
fruit_prices = {"Orange": 4, "Grapes": 3, "Banana": 2, "Cherry": 5}
```
**Output:**
```text
5
['Apple', 'Cherry', 'Grapes', 'Orange']
[2, 3, 5, 5]
```

### `increase_prices(fruit_prices: dict) -> None`
Increase the prices of every fruit by 20% and round to two decimal places. Modify the dictionary in place.

### Examples
**Input:**
```python
fruit_prices = {"Orange": 4, "Grapes": 3, "Banana": 2, "Cherry": 5}
```
**Output:**
```python
# The dictionary should be modified in place to:
{'Banana': 2.4, 'Cherry': 6.0, 'Grapes': 3.6, 'Orange': 4.8}
```

### `dict_from_string(string: str, key_type, value_type)`
Convert a string with comma-separated key-value pairs into a dictionary, converting the keys and values to the specified types.

### Examples
**Input:**
```python
string = "Apple,2\nBanana,3\nOrange,4\nGrapes,3\nPapaya,5"
key_type = str
value_type = int
```
**Output:**
```python
{'Apple': 2, 'Banana': 3, 'Grapes': 3, 'Orange': 4, 'Papaya': 5}
```

### `dict_to_string(D: dict) -> str`
Convert a dictionary back into a string with each key-value pair on a new line, using comprehensions.
*(Note: You are not allowed to use `if` statements or loops for this function, use comprehensions).*

### Examples
**Input:**
```python
D = {'Apple': 2, 'Banana': 3, 'Orange': 4, 'Grapes': 3, 'Papaya': 5}
```
**Output:**
```text
"Apple,2\nBanana,3\nOrange,4\nGrapes,3\nPapaya,5"
```
