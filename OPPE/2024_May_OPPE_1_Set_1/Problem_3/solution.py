from collections import Counter


def most_occuring_first_letter(passage: str) -> str:
    '''
    Returns the letter which occurs most frequently
    as the first letter of any word.(case insensitive)

    Args:
        passage (str): A multi-line string representing the passage.

    Returns:
        str: The most frequently occurring first letter in lowercase.
    '''
    first_letters = [word[0].lower() for word in passage.split()]
    return Counter(first_letters).most_common(1)[0][0]
    return max(set(first_letters), key=first_letters.count)