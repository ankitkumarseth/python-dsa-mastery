import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_analyze_bookings():
    bookings = {
        "PNR112": {
            "coach_type": "3AC",
            "ticket_rate": 900,
            "passengers": [("Rahul", "UB"), ("Baskar", None)]
        },
        "PNR123": {
            "coach_type": "2AC",
            "ticket_rate": 1500,
            "passengers": [("Amit", "LB"), ("Ravi", "UB")]
        },
        "PNR456": {
            "coach_type": "3AC",
            "ticket_rate": 800,
            "passengers": [("Priya", "MB"), ("Neha", None)]
        },
        "PNR789": {
            "coach_type": "SL",
            "ticket_rate": 500,
            "passengers": [("Vikram", "UB"), ("Kiran", "MB"), ("Surya", "SU")]
        },
    }

    assert solution.analyze_bookings(bookings, "ticket_prices") == {'PNR112': 1800, 'PNR123': 3000, 'PNR456': 1600, 'PNR789': 1500}
    assert solution.analyze_bookings(bookings, "total_revenue") == 7900
    
    expected_berths = {'LB': 1, 'MB': 2, 'SL': 0, 'SU': 1, 'UB': 3, None: 2}
    assert solution.analyze_bookings(bookings, "berth_preference_count") == expected_berths
    
    expected_coaches = {'2AC': 2, '3AC': 4, 'SL': 3}
    assert solution.analyze_bookings(bookings, "coach_type_count") == expected_coaches
