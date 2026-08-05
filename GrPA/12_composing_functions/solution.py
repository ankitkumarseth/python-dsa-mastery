def index_of_first_occurance(row: list, elem):
    """Given a list find the index of first occurance of `elem` in it

Example Input:
index_of_first_occurance([0, 0, 1, 1, 0], 1)

Expected Output:
2"""
    pass

def index_of_last_occurance(row: list, elem):
    """Given a list find the index of last occurance of `elem` in it.
Hint: use index_of_first_occurance with reversal.

Example Input:
index_of_last_occurance([0, 0, 1, 1, 0], 1)

Expected Output:
3"""
    pass

def is_valid_coordinate(x: int, y: int, M):
    """Checks if the x,y is a valid corrdinate(indices) in the matrix M(list of list). Assume coordinates are non-negative

Example Input:
is_valid_coordinate(2, 5, matrix)

Expected Output:
False"""
    pass

def valid_adjacent_coordinates(x: int, y: int, M):
    """Create a set of valid adjacent coordinates(indices) given x,y and a matrix M

Example Input:
valid_adjacent_coordinates(2, 2, matrix)

Expected Output:
{(1, 2), (2, 1), (2, 3), (3, 2)}"""
    pass

def next_coordinate_with_value(curr_coords, value, M, prev_coords=None):
    """Find the coordinate(indices) of the next coordinate that has the `value` in it. For the starting coordinate the prev_coords would be None

Example Input:
next_coordinate_with_value((2, 2), 1, matrix, (2, 1))

Expected Output:
(2, 3)"""
    pass

def get_path_coordinates(M):
    """Given the matrix m, find the path formed by 1 from the last row to the first row.

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
[(4, 1), (4, 0), (3, 0), (2, 0), (2, 1), (2, 2), (2, 3), (1, 3), (0, 3), (0, 2)]"""
    pass

def print_path(M):
    """Example Input:
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
(0, 2)"""
    pass

def alternate_path(M):
    """Example Input:
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
]"""
    pass

def count_path(M):
    """Example Input:
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
]"""
    pass

def mirror_horizontally(M):
    """Example Input:
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
]"""
    pass

def mirror_vertically(M):
    """Example Input:
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
]"""
    pass