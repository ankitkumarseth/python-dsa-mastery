import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_analyse_sales_data():
    sales_data = [
       {"product_id": "P101", "units_sold": 50, "revenue": 400},
       {"product_id": "P102", "units_sold": 30, "revenue": 900},
       {"product_id": "P101", "units_sold": 70, "revenue": 600},
       {"product_id": "P103", "units_sold": 120, "revenue": 600}
    ]

    assert solution.analyse_sales_data(sales_data, "total_revenue") == 2500
    assert solution.analyse_sales_data(sales_data, "product_wise_total_units_and_revenue") == {'P101': (120, 1000), 'P102': (30, 900), 'P103': (120, 600)}
    assert solution.analyse_sales_data(sales_data, "top_selling_product") == "P101"
    
    avg_price = solution.analyse_sales_data(sales_data, "average_product_price")
    assert avg_price == {'P101': 8.33, 'P102': 30.0, 'P103': 5.0}
