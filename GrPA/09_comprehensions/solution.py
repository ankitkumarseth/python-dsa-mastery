def sum_of_squares(numbers):
    """
    Example Input:
    sum_of_squares([1, 2, 3, 4])

    Expected Output:
    30
    """
    return sum( n ** 2 for n in numbers)

def total_cost(cart):
    """
    Example Input:
    total_cost([(1, 2), (3, 4), (1, 5)])

    Expected Output:
    19
    """
    return sum(quantity * price for quantity, price in cart)

def abbreviation(sentence):
    """
    Example Input:
    abbreviation("ordinary wizarding levels")

    Expected Output:
    O.W.L.
    """
    return ''.join(w[0].upper()+'.' for w in sentence.split())

def palindromes(words):
    """
    Example Input:
    palindromes(["moon", "noon", "dad", "dog", "cat", "madam"])

    Expected Output:
    ['noon', 'dad', 'madam']
    """
    # return list(filter(lambda w: w == w[::-1], words))
    return [w for w in words if w == w[::-1]]

def all_chars_from_big_words(sentence):
    """
    Example Input:
    all_chars_from_big_words("List comprehensions are a good start for functional programming")

    Expected Output:
    {'a', 'c', 'e', 'f', 'g', 'h', 'i', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u'}
    """
    return {char for word in sentence.lower().split() if len(word) > 5 for char in word}
    # return set(''.join(filter(lambda w: len(w) > 5, sentence.lower().split())))

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
    return [i for inner_list in lol for i in inner_list]

def unflatten(items, n_rows):
    """
    Example Input:
    unflatten([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4], 3)

    Expected Output:
    [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    """
    cols = len(items) // n_rows
    return [items[i * cols : (i + 1) * cols] for i in range(n_rows)]

def make_identity_matrix(m):
    """
    Example Input:
    make_identity_matrix(3)

    Expected Output:
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    # M = [[0] * m for _ in range(m)]
    # for i in range(m):
    #     for j in range(m):
    #         if i == j:
    #             M[i][j] = 1
    # return M
    return [[1 if i == j else 0 for j in range(m)] for i in range(m)]

def make_lower_triangular_matrix(m):
    """
    Example Input:
    make_lower_triangular_matrix(3)

    Expected Output:
    [[1, 0, 0], [1, 2, 0], [1, 2, 3]]
    """
    return [[j+1 if i >= j else 0 for j in range(m)] for i in range(m)]
