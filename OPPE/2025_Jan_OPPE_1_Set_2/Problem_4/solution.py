def merge_dictionaries(d1:dict, d2:dict):
    """
    Merges two dictionaries by summing values of common keys.

    If a key exists in both `d1` and `d2`, their values are summed.
    Keys that are unique to one dictionary are included as-is in the result.

    Args:
        d1 (dict): The first dictionary, where values are integers or floats.
        d2 (dict): The second dictionary, where values are integers or floats.

    Returns:
        dict: A new dictionary containing all keys from both `d1` and `d2`.
        Values for overlapping keys are summed, while unique keys retain their original values.

    """
    ...
