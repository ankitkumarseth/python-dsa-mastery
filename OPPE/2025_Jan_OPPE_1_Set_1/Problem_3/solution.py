def make_dict_from_elems_in_index(keys, values, index:int)-> dict:
    '''
    Returns a dictionary with one key and value pair
    taken from the given index of keys and values list.

    Eg:
    >>> keys = ['apple', 'banana', 'cherry']
    >>> values = [10, 20, 30, 40]
    >>> make_dict_from_elems_in_index(keys, values, 1) 
    {'banana': 20}
    >>> make_dict_from_elems_in_index(keys, values, -1) 
    {'cherry': 40}

    Args:
        keys (list): The list with the keys.
        values (list): The list with the values.
        index (int): An integer

    Returns:
        dict: Dictionary with only one key-value pair, where the key and value are taken from the given index.
    '''
    ...
