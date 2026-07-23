def index_of_first_occurance(row: list, elem):
    '''
    Given a list find the index of first occurance of `elem` in it

    Example Input:
    index_of_first_occurance([0, 0, 1, 1, 0], 1)

    Expected Output:
    2
    '''
    ...

def index_of_last_occurance(row: list, elem):
    '''
    Given a list find the index of last occurance of `elem` in it.
    Hint: use index_of_first_occurance with reversal.

    Example Input:
    index_of_last_occurance([0, 0, 1, 1, 0], 1)

    Expected Output:
    3
    '''
    ...

def is_valid_coordinate(x: int, y: int, M):
    '''
    Checks if the x,y is a valid corrdinate(indices) in the matrix M(list of list). Assume coordinates are non-negative

    Example Input:
    is_valid_coordinate(2, 5, matrix)

    Expected Output:
    False
    '''
    ...

def valid_adjacent_coordinates(x: int, y: int, M):
    '''
    Create a set of valid adjacent coordinates(indices) given x,y and a matrix M

    Example Input:
    valid_adjacent_coordinates(2, 2, matrix)

    Expected Output:
    {(1, 2), (2, 1), (2, 3), (3, 2)}
    '''
    return {
      (x1, y1)
      for x1, y1 in ... # all the possible adjacent coordinates
      if is_valid_coordinate(x1, y1, M)
    }

def next_coordinate_with_value(curr_coords, value, M, prev_coords=None):
    '''
    Find the coordinate(indices) of the next coordinate that has the `value` in it. For the starting coordinate the prev_coords would be None

    Example Input:
    next_coordinate_with_value((2, 2), 1, matrix, (2, 1))

    Expected Output:
    (2, 3)
    '''
    ...

def get_path_coordinates(M):
    '''
    Given the matrix m, find the path formed by 1 from the last row to the first row.
    '''
    x_start, x_end = len(M)-1, 0
    y_start, y_end = index_of_last_occurance(M[-1], 1), index_of_first_occurance(M[0], 1)
    ...

def print_path(M):
    '''
    Example Output:
    (4, 1)
    (4, 0)
    ...
    (0, 2)
    '''
    path = get_path_coordinates(M)
    ...

def alternate_path(M):
    '''
    Example Output State:
    [
        [0, 0, 2, 1],
        [0, 0, 0, 2],
        ...
    ]
    '''
    path = get_path_coordinates(M)
    ...

def count_path(M):
    '''
    Example Output State:
    [
        [0, 0, 10, 9],
        [0, 0, 0, 8],
        ...
    ]
    '''
    path = get_path_coordinates(M)
    ...

def mirror_horizontally(M):
    '''
    Example Output State:
    [
      [0, 1, 0, 1, 0],
      [0, 1, 1, 1, 0],
      ...
    ]
    '''
    path = get_path_coordinates(M)
    ...

def mirror_vertically(M):
    '''
    Example Output State:
    [
      [0, 1, 0, 1, 1],
      [0, 1, 1, 1, 0],
      ...
    ]
    '''
    path = get_path_coordinates(M)
    ...
