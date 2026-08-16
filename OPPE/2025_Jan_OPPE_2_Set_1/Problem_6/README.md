# Railway Ticket Booking Analysis

You are building a railway ticket analysis system that extracts information about the ticket bookings.
The booking data is represented as a dictionary of dictionaries, where:
- The key is the PNR number (str) representing the unique booking reference.
- The value is a dictionary containing:
  - `coach_type` (str): Type of the coach ("1AC", "2AC", "3AC", "SL", or "1C").
  - `ticket_rate` (int): Price for one person.
  - `passengers` (list of tuples): A list containing tuples with:
    - `passenger_name` (str): Name of the passenger.
    - `berth_preference` (str): Preference of the berth ("UB", "LB", "MB", "SU", "SL" or `None`).

Implement a function `analyze_bookings(bookings, task)` where task can be one of the following:

- `ticket_prices`: Computes a dictionary where the keys are the PNR numbers and the values are the total ticket price for each PNR.
- `total_revenue`: Returns the total revenue generated from all ticket bookings.
- `berth_preference_count`: Returns the count of passengers in each berth preference as a dictionary with berth_preference as the key and the number of passengers preferred that berth as value. Include all the possible berth preferences in the output dictionary and let the value be zero if not exists.
- `coach_type_count`: Returns a count of passengers in each coach type as a dictionary with coach_type as the key and the number of passengers in that coach as value. Only include the coach types that are available in the bookings dictionary in the output.

### Example
```python
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

print(analyze_bookings(bookings, "ticket_prices")) 
# Output: {'PNR112': 1800, 'PNR123': 3000, 'PNR456': 1600, 'PNR789': 1500}

print(analyze_bookings(bookings, "total_revenue")) 
# Output: 7900

print(analyze_bookings(bookings, 'berth_preference_count')) 
# Output: {'LB': 1, 'MB': 2, 'SL': 0, 'SU': 1, 'UB': 3, None: 2}

print(analyze_bookings(bookings, 'coach_type_count')) 
# Output: {'2AC': 2, '3AC': 4, 'SL': 3}
```
