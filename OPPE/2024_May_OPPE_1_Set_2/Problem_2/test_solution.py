import os, importlib.util
SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_matrix():
    m1 = [[1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 1, 1]]
    assert solution.row_index_with_most_number_of_zeros(m1) == 0
    m2 = [[1, 1, 1, 1], [0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 0, 0]]
    assert solution.row_index_with_most_number_of_zeros(m2) == 3
    m3 = [[1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 1]]
    assert solution.row_index_with_most_number_of_zeros(m3) == 1
