from collections import defaultdict

def total_price(fruit_prices: dict, purchases) -> float:
    """Compute the fruit prices give the quantity of each fruit. Do not use the sum function.

Arguments:
fruit_prices: dict - fruit name as key and price as value
purchases: list[tuple] - as list of tuples of (fruit, quantity)

Return:
total_price: float

Example Input:
total_price(
    {'Apple': 2.0, 'Banana': 3.0, 'Orange': 4.0, 'Grapes': 3.0, 'Papaya': 5.0},
    [("Apple", 3), ("Orange", 5), ("Grapes", 4)]
)

Expected Output:
38.0"""
    pass

def total_price_no_loops(fruit_prices: dict, purchases) -> float:
    """Compute the total price without loops.

Example Input:
total_price_no_loops(
    {'Apple': 2.0, 'Banana': 3.0, 'Orange': 4.0, 'Grapes': 3.0, 'Papaya': 5.0},
    [("Apple", 3), ("Orange", 5), ("Grapes", 4)]
)

Expected Output:
38.0"""
    pass

def find_cheapest_fruit(fruit_prices: dict) -> str:
    '''Find the cheapest fruit from the fruit_prices dict, do not use min function

Arguments:
fruit_prices: dict - fruit name as key and price as value

Return:
cheapest_fruit: str - the fruit with the lowest price

Example Input:
find_cheapest_fruit({'Apple': 7, 'Banana': 3, 'Orange': 4, 'Grapes': 6, 'Papaya': 5})

Expected Output:
"Banana"'''
    pass

def find_cheapest_fruit_no_loops(fruit_prices: dict) -> str:
    '''Find the cheapest fruit using min function. Do not use loops

Example Input:
find_cheapest_fruit_no_loops({'Apple': 7, 'Banana': 3, 'Orange': 4, 'Grapes': 6, 'Papaya': 5})

Expected Output:
"Banana"'''
    pass

def group_fruits(fruits: list):
    """Group the fruits based on the first letter of the names. Assume first letters will be upper case.

Arguments:
fruits - list: list of fruit names

Return:
dict: dict with the first letters as keys and list of fruits sorted in ascending order as values.

Example Input:
group_fruits([
  "Avocado", "Apple", "Banana",
  "Blackberry", "Cherry", "Cranberry",
  "Grape", "Mango"
])

Expected Output:
{'A': ['Apple', 'Avocado'], 'B': ['Banana', 'Blackberry'], 'C': ['Cherry', 'Cranberry'], 'G': ['Grape'], 'M': ['Mango']}"""
    pass

def bin_fruits(fruit_prices):
    """Classify the fruits as cheap, affordable and costly based on the fruit prices. Create a dictionary with the classification as keys and a set of fruits in that category.

cheap - less than 3 (not inclusive)
affordable - between 3 and 6 (both inclusive)
costly - greater than 6 (not inclusive)

Arguments:
fruit_prices: dict - dictionary with fruits as keys and prices as values

Return:
binned_fruits: dict - dictionary with category as key and a set of fruits in that category as values.

Example Input:
bin_fruits({'Apple': 7, 'Banana': 3, 'Orange': 4, 'Grapes': 6, 'Papaya': 5, 'Mango': 2, 'Amla': 1, 'Jackfruit': 10})

Expected Output:
{'affordable': {'Banana', 'Grapes', 'Orange', 'Papaya'}, 'cheap': {'Amla', 'Mango'}, 'costly': {'Apple', 'Jackfruit'}}"""
    pass