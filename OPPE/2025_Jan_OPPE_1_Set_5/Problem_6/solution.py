def average_hold_time(data: list, key: str) -> float:
    """Computes the average duration a specific key is held before release.
    
    Assume the key is present at least once in the data.
    
    Args:
        data (list): List of tuples (key, time) with alternating press/release actions.
        key (str): The key for which to calculate the average hold time.

    Returns:
        float: The average hold time for the key.
    """
    ...
    
def average_transition_time(data: list, key1: str, key2: str) -> float:
    """Computes the average time taken to transition between two specific keys.

    Transition time is the time between release of key1 and the press of key2.
    
    Args:
        data (list): List of tuples (key, time) with alternating press/release actions.
        key1 (str): The first key.
        key2 (str): The second key.

    Returns:
        float: The average transition time between key1 and key2.
    """
    ...
    
def get_typed_text(data: list) -> float:
    """Computes th final text typed after the given key strokes.

    Args:
        data (list): List of tuples (key, time) with alternating press/release actions.

    Returns:
        float: The final typed text after considering the backpaces.
    """
    ...
    
def words_per_minute(data: list) -> float:
    """Computes the words per minute based on the total time taken for key press events.

    The total time is the duration between the first key press and the last key release.
    
    Args:
        data (list): List of tuples (key, time) with alternating press/release actions.

    Returns:
        float: The words per minute rate.
    """
    ...
