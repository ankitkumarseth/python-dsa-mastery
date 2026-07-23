def process_grocery_list(grocery_list:list, request:str):
    """Process the grocery list as per the request.

    Args:
        grocery_list (list[dict]) - A list of dictionary with the keys
            "name", "quantity" and "price", where "price" is the amount of 
            one unit of the item.
        request: (str) - A string containing one of the following request.
            - 'total_bill_amount'
            - 'max_quantity_item'
            - 'sort_by_total_amount'

    Returns: 
        The output corresponding to the request.
    """
    ...
