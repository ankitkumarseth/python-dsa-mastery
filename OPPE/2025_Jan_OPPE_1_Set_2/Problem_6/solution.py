def employees_with_salary_above(employees:list, min_salary:int):
    """Returns the employees names with salary greater than are equal to the given salary.
    
    Args:
        employees (list[dict]):
            list of dictionary of employees with 
            the keys name, salary and department.
        min_salary (int): The cutoff salary.

    Returns:
        list[str]: 
            list of names of the employees with salary 
            greater than or equal to the cutoff
            in the order of occurance.
    """
    ...

def total_salary_in_department(employees:list, department:str):
    """Returns the total salary of all the employees in the department.
    
    Args:
        employees (list[dict]):
            list of dictionary of employees with 
            the keys name, salary and department.
        department (str): The department to find the total salary.

    Returns:
        int: The total salary of the employees in the given department.
    """
    ...

def ceil_to_five_hundreds(num: int):
    """Given an integer, increase it to the next multiple of 500 if it is not a multiple of 500.

    Args:
        num (int): The number to increment.
    
    Returns:
        int: The number ceiled to the next five hundreds.

    Examples:
    >>> ceil_to_five_hundreds(24500)
    24500
    >>> ceil_to_five_hundreds(24600)
    25000
    >>> ceil_to_five_hundreds(24400)
    24500
    """
    ...

def max_salary_after_increment_in_department(employees:list, department:str, inc_percent:int):
    """Returns the maximum salary in the given department after increment.
    
    The Maximum salary is incremented with the given percentage,
    rounded to the nearest integer and ceiled to the next five hundreds

    Rounding can be done using round function.
    
    Args:
        employees (list[dict]):
            list of dictionary of employees with 
            the keys name, salary and department.
        department (str): The department to find the maximum salary.
        inc_percent (int): Percentage of increment in the salary.

    Returns:
        int: 
            The maximum salary in the given department after increment 
            and ceiling it to the next five hundreds.
    """
    ...
