"""
🎓 AGENT FEEDBACK:
For the first time since we started, I have absolutely zero "Pythonic Alternatives" to add to this file!
Every single function here is written exactly how a Senior Python Engineer would write it:
- Slicing arithmetic (`items[k:] + items[:k]`) instead of messy loops
- `items[:] =` for pure in-place mutation
- `[::-1].index()` for reverse lookups
- `k % len(items)` for circular rotation

Flawless execution.
"""

def swap_halves(items):
    """
    Example Input:
    swap_halves((1, 2, 3, 4, 5, 6))

    Expected Output:
    (4, 5, 6, 1, 2, 3)
    """
    return items[len(items) // 2 :] +  items[:len(items) // 2]

def swap_at_index(items, k):
    """
    Example Input:
    swap_at_index((1, 2, 3, 4, 5, 6), 1)

    Expected Output:
    (3, 4, 5, 6, 1, 2)
    """
    return items[k+1:] + items[:k+1]

def rotate_k(items, k=1):
    """
    Example Input:
    rotate_k((1, 2, 3, 4, 5, 6), 4)

    Expected Output:
    (3, 4, 5, 6, 1, 2)
    """
    k = k % len(items)
    return items[-k:] + items[:-k]

def first_and_last_index(items, elem):
    """
    Example Input:
    first_and_last_index((1, 2, 3, 1, 5, 6), 1)

    Expected Output:
    (0, 3)
    """
    return items.index(elem), len(items) - items[::-1].index(elem) - 1

def reverse_first_and_last_halves(items):
    """
    Example Input:
    reverse_first_and_last_halves([1, 2, 3, 4, 5, 6, 7, 8])

    Expected Output:
    [4, 3, 2, 1, 8, 7, 6, 5]
    """
    mid = len(items) // 2
    items[:] = items[:mid][::-1] +  items[mid:][::-1]
