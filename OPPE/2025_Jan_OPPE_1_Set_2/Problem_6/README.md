# Employee Data Analysis

A list of employee records as a list of dictionaries with keys `name`, `department` and `salary`. Implement the following functions.

- `employees_with_salary_above(employees:list[dict], min_salary:int)->str` - Returns the list of names of employees whose salary is greater than or equal to the given minimum salary.
- `total_salary_in_department(employees:list[dict], department: str)->int` - Returns the total salary expense in the given department.
- `ceil_to_five_hundreds(num:int)->int` - Returns a number ceiled to the next five hundreds.
- `max_salary_after_increment_in_department(employees:list[dict], department:str, inc_percent: int) -> int` - Returns the maximum salary in the given department after increment with the given percentage and ceiling it to the next five hundreds.

**NOTE:** This is a function type question, you don't have to take input or print the output, just have to complete the required function definition. You can define helper functions if needed, but the actual solution should be in the given function template.

### Example

```python
employees = [
    {'name': 'Alice', 'department': 'HR', 'salary': 50000},
    {'name': 'Bob', 'department': 'Engineering', 'salary': 70000},
    {'name': 'Charlie', 'department': 'HR', 'salary': 45000},
    {'name': 'David', 'department': 'Engineering', 'salary': 60000},
    {'name': 'Eve', 'department': 'Marketing', 'salary': 55000},
]
print(employees_with_salary_above(employees, 60000)) # ['Bob','David']
print(total_salary_in_department(employees, 'HR')) # 95000
print(ceil_to_five_hundreds(25100)) # 25500
print(max_salary_after_increment_in_department(employees, 'Engineering', 7)) # after increment 74900, after rounding 75000
```
