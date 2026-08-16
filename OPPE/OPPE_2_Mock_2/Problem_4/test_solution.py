import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_consistent_sales_increase():
    # Test case 1
    file1 = os.path.join(os.path.dirname(__file__), 'test_input_1.csv')
    assert solution.consistent_sales_increase(file1) == "Chennai"

    # Test case 2
    file2 = os.path.join(os.path.dirname(__file__), 'test_input_2.csv')
    assert solution.consistent_sales_increase(file2) == "Ahemdabad"
