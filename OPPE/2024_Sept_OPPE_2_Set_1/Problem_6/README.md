# Shopping List

Given a list of dictionaries with keys: `name`, `quantity`, and `price` for each item in a grocery list, write a function that does the following based on the request:

- `total_bill_amount`: Find the total bill amount by summing the price multiplied by the quantity for each item.
- `max_quantity_item`: Find the name of the item with the maximum quantity. If there are multiple items with the same quantity, return the first one.
- `sort_by_total_amount`: Sort the list by the highest total amount for an item (calculated as `price * quantity`). If two items have the same total amount, break the tie by sorting by `name` in ascending order.

**NOTE:** This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

### Example

```python
grocery_list = [
    {'name': 'apple', 'quantity': 2, 'price': 3},
    {'name': 'banana', 'quantity': 5, 'price': 2},
    {'name': 'carrot', 'quantity': 4, 'price': 1}
]
```
- **total_bill_amount** -> 6+10+4 = 20
- **max_quantity_item** -> 'banana'
- **sort_by_total_amount** -> sorted list of dict in the order 'banana', 'apple' and 'carrot'
