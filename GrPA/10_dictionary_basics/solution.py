def dictionary_operations(fruit_prices: dict, fruits: list):
    """
    Perform a series of operations on the given fruit_prices dictionary.
    Note: Do not use loops or conditionals.

    Example:
        fruits = ["Apple", "Orange", "Grapes", "Banana", "Cherry"]
        fruit_prices = {"Orange": 4, "Grapes": 3, "Banana": 2, "Cherry": 5}

        Expected Prints:
        5
        ['Apple', 'Cherry', 'Grapes', 'Orange']
        [2, 3, 5, 5]
    """
    # add the fruit fruits[0] to fruit_prices with cost 3
    fruit_prices[fruits[0]] = 3

    # modify the cost of fruits[1] as 2 in fruit_prices
    fruit_prices[fruits[1]] = 2

    # increase the cost of fruits[2] by 2 in fruit_prices
    fruit_prices[fruits[2]] += 2

    # delete both key and value for fruits[3] from fruit_prices
    del fruit_prices[fruits[3]]
    # 💡 Pro-Tip: `del` is perfect if you are 100% sure the key exists. 
    # If you aren't sure, use `.pop()` with a default value to prevent a KeyError:
    # fruit_prices.pop(fruits[3], None)

    # print the price of fruits[4]
    print(fruit_prices[fruits[4]])

    # print the names of fruits in fruit prices as a list sorted in ascending order
    print(sorted(fruit_prices.keys()))

    # print the prices of the fruits as a list sorted in ascending order.
    print(sorted(fruit_prices.values()))


def increase_prices(fruit_prices: dict) -> None:
    """
    Increase the prices of every fruit by 20 percent and round to two decimal places
    Modify inplace, do not return anything.

    Example:
        fruit_prices = {"Orange": 4, "Grapes": 3, "Banana": 2, "Cherry": 5}
        # Becomes: {'Orange': 4.8, 'Grapes': 3.6, 'Banana': 2.4, 'Cherry': 6.0}
    """
    for key, value in fruit_prices.items():
        fruit_prices[key] = round(value + value/5, 2)
        # 🐍 Pythonic Alternative: You can just multiply by 1.2 instead of `value + value/5`
        # fruit_prices[key] = round(value * 1.2, 2)

def dict_from_string(string: str, key_type, value_type):
    """
    Create a dictionary out of a comma-separated key-value string.

    Example:
        string = "Apple,2\nBanana,3\nOrange,4\nGrapes,3\nPapaya,5"
        # Returns: {'Apple': 2, 'Banana': 3, 'Orange': 4, 'Grapes': 3, 'Papaya': 5}
    """
    return {key_type(key): value_type(value) for key, value in (item.split(',') for item in string.split('\n'))}


def dict_to_string(D: dict) -> str:
    """
    Convert dictionary back to string format using comprehensions.
    Note: Do not use loops or conditionals.
    """
    return '\n'.join(f"{k},{v}" for k,v in D.items())
