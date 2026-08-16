import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_book_analysis():
    data = [
        {"book_id": "X1", "pages": 540, "rating": 4.9},
        {"book_id": "X2", "pages": 96,  "rating": 4.6},
        {"book_id": "X3", "pages": 1225,"rating": 4.4},
        {"book_id": "X4", "pages": 328, "rating": 4.2},
        {"book_id": "X5", "pages": 180, "rating": 3.9},
        {"book_id": "X6", "pages": 1225,"rating": 4.3},
    ]

    assert solution.book_analysis(data, "average_rating") == 4.38
    assert solution.book_analysis(data, "average_pages") == 599.0
    assert solution.book_analysis(data, "longest_book") == "X3"
    assert solution.book_analysis(data, "above_average_books") == {'X3'}
