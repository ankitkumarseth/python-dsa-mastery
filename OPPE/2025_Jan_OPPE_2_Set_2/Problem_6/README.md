# Employee Task Analysis

Given a list of dictionaries representing employees where each dictionary contains the keys `employee_id`, `tasks_completed`, and `hours_worked`, write a function that does the following based on the given task:

- `total_tasks_completed`: Compute the total number of tasks completed by all employees combined.
- `most_efficient_employee`: Determine the id of the employee with the highest ratio of `tasks_completed` to `hours_worked`. If there are ties, break by the highest number of tasks completed.
- `sort_by_hours_worked`: Get the list of employee ids sorted by the number of hours worked from the highest to the lowest and break ties using the highest number of tasks completed.
- `productive_team_members`: Filter and return a list of employee ids of employees who have completed 20 or more tasks in the order that they are present in the employee list.

NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

### Example
```python
employee_list = [
    {'employee_id': 1, 'tasks_completed': 30, 'hours_worked': 40},
    {'employee_id': 2, 'tasks_completed': 60, 'hours_worked': 90},
    {'employee_id': 3, 'tasks_completed': 60, 'hours_worked': 100},
    {'employee_id': 4, 'tasks_completed': 50, 'hours_worked': 100},
    {'employee_id': 5, 'tasks_completed': 10, 'hours_worked': 30},
]
```

- `total_tasks_completed` -> `30+60+60+50+10 = 210`
- `most_efficient_employee` -> `1` 
  - Employee 1 efficiency = 30/40 = 0.75
  - Employee 2 efficiency = 60/90 = 0.66
  - Employee 3 efficiency = 60/100 = 0.60
  - Employee 4 efficiency = 50/100 = 0.50
  - Employee 5 efficiency = 10/30 = 0.33
- `sort_by_hours_worked` -> `[3, 4, 2, 1, 5]` (3 and 4 have more number of hours worked but 3 has completed most tasks)
- `productive_team_members` -> `[1, 2, 3, 4]` (5 has completed less than 20 tasks, thus not included.)
