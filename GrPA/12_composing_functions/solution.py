def index_of_first_occurance(row: list, elem):
    '''
    Given a list find the index of first occurance of `elem` in it

    Example Input:
    index_of_first_occurance([0, 0, 1, 1, 0], 1)

    Expected Output:
    2
    '''
    return row.index(elem)

def index_of_last_occurance(row: list, elem):
    '''
    Given a list find the index of last occurance of `elem` in it.
    Hint: use index_of_first_occurance with reversal.

    Example Input:
    index_of_last_occurance([0, 0, 1, 1, 0], 1)

    Expected Output:
    3
    '''
    return len(row) - row[::-1].index(elem) - 1

def is_valid_coordinate(x: int, y: int, M):
    '''
    Checks if the x,y is a valid corrdinate(indices) in the matrix M(list of list). Assume coordinates are non-negative

    Example Input:
    is_valid_coordinate(2, 5, matrix)

    Expected Output:
    False
    '''
    return 0 <= x < len(M) and 0 <= y < len(M[0])

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
      for x1, y1 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)) # all the possible adjacent coordinates
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
    x, y = curr_coords
    valid_neighbors = valid_adjacent_coordinates(x, y, M) - {prev_coords}
    return next((x1, y1) for x1, y1 in valid_neighbors if M[x1][y1] == value)
    # return tuple((x1, y1) for x1, y1 in valid_neighbors if M[x1][y1] == value)[0]
    # or
    # for x1, y1 in valid_neighbors:
    #     if M[x1][y1] == value:
    #         return x1, y1
    # return None


def get_path_coordinates(M):
    '''
    Given the matrix m, find the path formed by 1 from the last row to the first row.

    Example Input:
    matrix = [
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 1, 0, 0]
    ]
    get_path_coordinates(matrix)

    Expected Output:
    [(4, 1), (4, 0), (3, 0), (2, 0), (2, 1), (2, 2), (2, 3), (1, 3), (0, 3), (0, 2)]
    '''
    x_start, x_end = len(M)-1, 0
    y_start, y_end = index_of_last_occurance(M[-1], 1), index_of_first_occurance(M[0], 1)

    curr_coords = (x_start, y_start)
    prev_coords = None
    path = [curr_coords]
    while curr_coords != (x_end, y_end):
        temp_coords = curr_coords
        curr_coords = next_coordinate_with_value(curr_coords, 1, M, prev_coords)
        prev_coords = temp_coords
        path.append(curr_coords)
    return path

def print_path(M):
    '''
    Example Input:
    matrix = [
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 1, 0, 0]
    ]
    print_path(matrix)

    Example Output:
    (4, 1)
    (4, 0)
    ...
    (0, 2)
    '''
    path = get_path_coordinates(M)
    print('\n'.join(map(str, path)))

def alternate_path(M):
    '''
    Example Input:
    matrix = [
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 1, 0, 0]
    ]
    alternate_path(matrix)

    Example Output State:
    [
        [0, 0, 2, 1],
        [0, 0, 0, 2],
        ...
    ]
    '''
    path = get_path_coordinates(M)
    for i in range(1, len(path) + 1):
        if i % 2 == 0:
            x,y = path[i-1]
            M[x][y] += 1

def count_path(M):
    '''
    Example Input:
    matrix = [
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 1, 0, 0]
    ]
    count_path(matrix)

    Example Output State:
    [
        [0, 0, 10, 9],
        [0, 0, 0, 8],
        ...
    ]
    '''
    path = get_path_coordinates(M)
    for i in range(1, len(path) + 1):
        x, y = path[i-1]
        M[x][y] = i

def mirror_horizontally(M):
    '''
    Example Input:
    matrix = [
      [0, 1, 0, 0, 0],
      [0, 1, 1, 1, 0],
      [0, 0, 0, 1, 0],
      [0, 0, 0, 1, 1]
    ]
    mirror_horizontally(matrix)

    Example Output State:
    [
      [0, 1, 0, 1, 0],
      [0, 1, 1, 1, 0],
      ...
    ]
    '''
    path = get_path_coordinates(M)
    rows = len(M)
    cols = len(M[0])
    for x,y in path:
        new_x, new_y = x, cols - y - 1
        M[new_x][new_y] = 1

def mirror_vertically(M):
    '''
    Example Input:
    matrix = [
      [0, 1, 0, 0, 0],
      [0, 1, 1, 1, 0],
      [0, 0, 0, 1, 0],
      [0, 0, 0, 1, 1]
    ]
    mirror_vertically(matrix)

    Example Output State:
    [
      [0, 1, 0, 1, 1],
      [0, 1, 1, 1, 0],
      ...
    ]
    '''
    path = get_path_coordinates(M)
    rows = len(M)
    cols = len(M[0])
    for x,y in path:
        new_x, new_y = rows - x - 1, y
        M[new_x][new_y] = 1
