min = None

def find_min(items:list):
    """
    Example Input:
    find_min([1, 2, 3, 4, -4])

    Expected Output:
    -4
    """
    minimum = items[0]
    for item in items:
        if item < minimum:
            minimum = item
    return minimum

def odd_increment_even_decrement_no_modify(items) -> list:
    """
    Example Input:
    odd_increment_even_decrement_no_modify([1, 2, 3, 4, 5, 6])

    Expected Output:
    [2, 1, 4, 3, 6, 5]
    """
    result = items[:]
    for i, item in enumerate(result):
        if item % 2 == 0:
            result[i] = item - 1
        else:
            result[i] = item + 1
    return result
    # Pythonic Alternative (List Comprehension):
    # return [item - 1 if item % 2 == 0 else item + 1 for item in items]

def odd_square_even_double_modify(items:list) -> list:
    """
    Example Input:
    odd_square_even_double_modify([1, 2, 3, 4, 5, 6])

    Expected Output:
    [1, 4, 9, 8, 25, 12]
    """
    for i ,item in enumerate(items):
        if item % 2 == 0:
            items[i] *= 2
        else:
            items[i] **= 2
    return items
    # Pythonic Alternative (In-place List Comprehension replacement using slice assignment):
    # items[:] = [item * 2 if item % 2 == 0 else item ** 2 for item in items]
    # return items

def more_than_two_unique_vowels(sentence):
    """
    Example Input:
    more_than_two_unique_vowels("functions,are,not,complicated")

    Expected Output:
    {'complicated', 'functions'}
    """
    words = sentence.split(',')
    vowels = 'aeiouAEIOU'
    result = set()
    for word in words:
        if len(set(word) & set(vowels)) > 2:
            result.add(word)
    return result
    # Pythonic Alternative (Set Comprehension):
    # return {word for word in sentence.split(',') if len(set(word) & set("aeiouAEIOU")) > 2}

def sum_of_list_of_lists(lol):
    """
    Example Input:
    sum_of_list_of_lists([
        [1, 2, 3, 4],
        [10, 20],
        [5],
    ])

    Expected Output:
    45
    """
    return sum(sum(lst) for lst in lol)

def flatten(lol):
    """
    Example Input:
    flatten([
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4]
    ])

    Expected Output:
    [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
    """
    return [item for inner_list in lol for item in inner_list]
    # Pythonic Alternative (Using sum with an empty list to concatenate):
    # return sum(lol, [])

def all_common(strings):
    """
    Example Input:
    all_common([
        "abcde",
        "bcdef",
        "cdefg",
    ])

    Expected Output:
    cde
    """
    result = set(strings[0])
    for i in range(len(strings)):
        result = result.intersection(set(strings[i]))
    return ''.join(sorted(result))

    # Pythonic Alternative 1 (Iterating directly):
    # result = set(strings[0])
    # for string in strings:
    #     result &= set(string) # &= is the shorthand for intersection!
    # return ''.join(sorted(result))
    
    # Pythonic Alternative 2 (Advanced Unpacking):
    # return ''.join(sorted(set.intersection(*map(set, strings))))

def vocabulary(sentences):
    """
    Example Input:
    vocabulary([
        "This is a car",
        "He is playing with a bat",
        "He and she are playing",
    ])

    Expected Output:
    {'a', 'and', 'are', 'bat', 'car', 'he', 'is', 'playing', 'she', 'this', 'with'}
    """
    result = set()
    for sentence in sentences:
        result |= set(sentence.lower().split())

    return result
    
    # Pythonic Alternative 1 (Nested Set Comprehension):
    # return {word for sentence in sentences for word in sentence.lower().split()}
