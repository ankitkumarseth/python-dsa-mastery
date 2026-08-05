# mapping


def is_greater_than_5(numbers: list) -> list:
    '''
    Given a list of numbers, return a list of bools corresponding to whether the number is greater than 5

    Example Input:
    is_greater_than_5([3, 4, 5, 6, 7])

    Expected Output:
    [False, False, False, True, True]
    '''
    return list(map(lambda x: x > 5, numbers))
    # return [x > 5 for x in numbers]

# filtering


def filter_less_than_5(numbers: list) -> list:
    '''
    Given an list of numbers, return a list of numbers that are less than 5

    Example Input:
    filter_less_than_5([3, 4, 5, 6, 7])

    Expected Output:
    [3, 4]
    '''
    return list(filter(lambda x: x < 5, numbers))
    # return [x for x in numbers if x < 5]

# aggregation with filtering


def sum_of_two_digit_numbers(numbers: list):
    '''
    Given a list of numbers find the sum of all two_digit_numbers.

    Example Input:
    sum_of_two_digit_numbers([8, 9, 10, 11, 12])

    Expected Output:
    33
    '''
    return sum(filter(lambda x: len(str(abs(x))) == 2, numbers))
    # return sum(x for x in numbers if len(str(abs(x))) == 2)

# aggregation with mapping


def is_all_has_a(words: list) -> bool:
    '''
    Given a list of words check if all words has the letter a(case insensitive) in it.

    Example Input:
    is_all_has_a(["Apple", "Orange", "Banana"])

    Expected Output:
    True
    '''
    return all(map(lambda x: 'a' in x.lower(), words))
    # 🐍 Comprehension Alternative:
    # return all('a' in word.lower() for word in words)

# enumerate


def print_with_numbering(items):
    '''
    Print a list in multiple lines with numbering.

    Example Input:
    print_with_numbering(["Apple", "Orange", "Banana"])

    Expected Output:
    1. Apple
    2. Orange
    3. Banana
    '''
    for i, v in enumerate(items, 1):
        print(f"{i}. {v}")

# zip


def parallel_print(countries, capitals):
    '''
    Print the countries and capitals in multiple line seperated by a hyphen with space around it.

    Example Input:
    parallel_print(
      ["United States", "Brazil", "Nigeria"],
      ["Washington, D.C.", "Brasilia", "Abuja"]
    )

    Expected Output:
    United States - Washington, D.C.
    Brazil - Brasilia
    Nigeria - Abuja
    '''
    for country, capital in zip(countries, capitals):
        print(f"{country} - {capital}")

# key value list to dict


def make_dict(keys, values):
    '''
    Create a dict with keys and values

    Example Input:
    make_dict("abcd", [1, 2, 3, 4])

    Expected Output:
    {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    '''
    return dict(zip(keys, values))
    # 🐍 Comprehension Alternative:
    # return {key: value for key, value in zip(keys, values)}

# enumerate with filtering and map


def indices_of_big_words(words) -> list:
    '''
    Given a list of words, find the indices of the big words(length greater than 5).

    Example Input:
    indices_of_big_words(["Apple", "Banana", "Orange", "Kiwi", "Cherry"])

    Expected Output:
    [1, 2, 4]
    '''
    # Use enumerate to guarantee we get the true index, even if there are duplicate words!
    return list(map(lambda item: item[0], filter(lambda item: len(item[1]) > 5, enumerate(words))))
    
    # 🐍 Comprehension Alternative:
    # return [i for i, word in enumerate(words) if len(word) > 5]

# zip with mapping and aggregation


def decode_rle(chars: str, repeats: list) -> str:
    '''
    Create a string with i-th char from chars repeated i-th value of repeats number of times.
    Note rle refers to Run-length encoding

    Example Input:
    decode_rle("abcd", [2, 4, 3, 1])

    Expected Output:
    aabbbbcccd
    '''
    return "".join(map(lambda x: x[0] * x[1], zip(chars, repeats)))
    
    # 🐍 Comprehension Alternative:
    # return "".join(char * count for char, count in zip(chars, repeats))
