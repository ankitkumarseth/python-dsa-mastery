import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_calculate_total_price():
    prices1 = os.path.join(os.path.dirname(__file__), 'shopdata1.csv')
    shopping1 = os.path.join(os.path.dirname(__file__), 'shopping1.csv')
    assert solution.calculate_total_price(prices1, shopping1) == 3156
    
    prices2 = os.path.join(os.path.dirname(__file__), 'shopdata2.csv')
    shopping2 = os.path.join(os.path.dirname(__file__), 'shopping2.csv')
    assert solution.calculate_total_price(prices2, shopping2) == 3242
