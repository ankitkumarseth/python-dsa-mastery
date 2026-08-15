import re
def is_all_same_word_twice(strings: list) -> bool:
    '''
    Checks if all strings follow the format where
    the same word is repeated exactly twice with a hyphen in-between them.

    Args:
        strings (list): A list of strings to be checked.

    Returns:
        bool: True if all strings are of the given format, otherwise False.
    '''
    pattern = re.compile(r"^([a-zA-Z]+)-\1$")
    return all(pattern.match(string) for string in strings)