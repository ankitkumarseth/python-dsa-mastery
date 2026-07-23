# GrPA Dictionary Applications

Implement the below functions to perform various operations on dictionaries.

### Functions to Implement

* **`total_price(fruit_prices: dict, purchases: list) -> float`**: Compute the total fruit price given the quantity of each fruit. Do not use the `sum` function.
### Examples
**Input:**
```python
total_price(
  {'Apple': 2.0, 'Banana': 3.0, 'Orange': 4.0, 'Grapes': 3.0, 'Papaya': 5.0},
  [("Apple", 3), ("Orange", 5), ("Grapes", 4)]
)
```
**Output:**
```text
38.0
```

* **`total_price_no_loops(fruit_prices: dict, purchases: list) -> float`**: Compute the total price without loops.
### Examples
**Input:**
```python
total_price_no_loops(
  {'Apple': 2.0, 'Banana': 3.0, 'Orange': 4.0, 'Grapes': 3.0, 'Papaya': 5.0},
  [("Apple", 3), ("Orange", 5), ("Grapes", 4)]
)
```
**Output:**
```text
38.0
```

* **`find_cheapest_fruit(fruit_prices: dict) -> str`**: Find the cheapest fruit from the `fruit_prices` dict. Do not use the `min` function.
### Examples
**Input:**
```python
find_cheapest_fruit({'Apple': 7, 'Banana': 3, 'Orange': 4, 'Grapes': 6, 'Papaya': 5})
```
**Output:**
```text
"Banana"
```

* **`find_cheapest_fruit_no_loops(fruit_prices: dict) -> str`**: Find the cheapest fruit using the `min` function. Do not use loops.
### Examples
**Input:**
```python
find_cheapest_fruit_no_loops({'Apple': 7, 'Banana': 3, 'Orange': 4, 'Grapes': 6, 'Papaya': 5})
```
**Output:**
```text
"Banana"
```

* **`group_fruits(fruits: list) -> dict`**: Group the fruits based on the first letter of the names. Assume first letters will be upper case. Return a dict with the first letters as keys and a list of fruits sorted in ascending order as values.
### Examples
**Input:**
```python
group_fruits([
    "Avocado", "Apple", "Banana",
    "Blackberry", "Cherry", "Cranberry",
    "Grape", "Mango"
])
```
**Output:**
```text
{'A': ['Apple', 'Avocado'], 'B': ['Banana', 'Blackberry'], 'C': ['Cherry', 'Cranberry'], 'G': ['Grape'], 'M': ['Mango']}
```

* **`bin_fruits(fruit_prices: dict) -> dict`**: Classify the fruits as cheap, affordable and costly based on the fruit prices.
  * cheap - less than 3 (not inclusive)
  * affordable - between 3 and 6 (both inclusive)
  * costly - greater than 6 (not inclusive)
### Examples
**Input:**
```python
bin_fruits({'Apple': 7, 'Banana': 3, 'Orange': 4, 'Grapes': 6, 'Papaya': 5, 'Mango': 2, 'Amla': 1, 'Jackfruit': 10})
```
**Output:**
```text
{'affordable': {'Banana', 'Grapes', 'Orange', 'Papaya'}, 'cheap': {'Amla', 'Mango'}, 'costly': {'Apple', 'Jackfruit'}}
```
