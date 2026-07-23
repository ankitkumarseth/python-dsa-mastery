# GrPA Min, Max, Sorted, Groupby

Implement all the given functions below according to the docstrings.

> [!WARNING]
> **Note:** For specific functions (`min_course_marks`, `max_course_marks`, `rollno_of_max_marks`, `sort_rollno_by_marks`, `count_students_by_cities`, `city_with_max_no_of_students`, `group_rollnos_by_cities`, `city_with_max_avg_course_mark`), you are **not** allowed to use `if` statements, `for`/`while` loops, or comprehensions! You must compose your logic using `min`, `max`, `sorted`, and your `groupby` / `apply_to_groups` helper functions.

### Functions to Implement

* **`groupby(data: list, key: callable) -> dict`**: Given a list of items, and a key, create a dictionary with the key as key function called on item and the list of items with the same key as the corresponding value. The order of items in the group should be the same order in the original list.
### Examples
**Input:**
```python
fruits = ["Apple", "Banana", "Avocado", "Amla", "Black berry", "Blue berry"]
groupby(fruits, lambda x: x[0])
```
**Output:**
```text
{'A': ['Apple', 'Avocado', 'Amla'], 'B': ['Banana', 'Black berry', 'Blue berry']}
```

* **`apply_to_groups(groups: dict, func: callable) -> dict`**: Apply a function to the list of items for each group.
### Examples
**Input:**
```python
groups = {"A": ["Apple", "Avocado"], "B": ["Banana", "Black berry", "Blue berry"]}
apply_to_groups(groups, len)
```
**Output:**
```text
{'A': 2, 'B': 3}
```

* **`min_course_marks(student_data: list, course: str) -> int`**: Return the min marks on a given course.
  > **Example Output:**
  > ```text
  > 1
  > ```

* **`max_course_marks(student_data: list, course: str) -> int`**: Return the max marks on a given course.
  > **Example Output:**
  > ```text
  > 98
  > ```

* **`rollno_of_max_marks(student_data: list, course: str) -> int`**: Return the rollno of student with max marks in a course.
  > **Example Output:**
  > ```text
  > 17
  > ```

* **`sort_rollno_by_marks(student_data: list, course1: str, course2: str, course3: str) -> list`**: Return a sorted list of rollno sorted based on their marks on the three course marks. `course1` is compared first, then `course2`, then `course3` to break ties. (Hint: use tuples comparison).
  > **Example Output:**
  > ```text
  > [7, 5, 1, 4, 3, 9, 2, 8, 10, 6]
  > ```

* **`count_students_by_cities(student_data: list) -> dict`**: Create a dictionary with city as key and number of students from each city as value.
  > **Example Output:**
  > ```text
  > {'Chennai': 3, 'Delhi': 5, 'Kolkata': 2, 'Mumbai': 7, 'Patna': 3}
  > ```

* **`city_with_max_no_of_students(student_data: list) -> str`**: Find the city with the maximum number of students.
  > **Example Output:**
  > ```text
  > Mumbai
  > ```

* **`group_rollnos_by_cities(student_data: list) -> dict`**: Create a dictionary with city as key and a sorted list of rollno of students that belong to that city as the value.
  > **Example Output:**
  > ```text
  > {'Chennai': [1, 4, 15], 'Delhi': [7, 9, 10, 16, 17], 'Kolkata': [8, 11], 'Mumbai': [3, 5, 6, 12, 13, 18, 20], 'Patna': [2, 14, 19]}
  > ```

* **`city_with_max_avg_course_mark(student_data: list, course: str) -> str`**: Find the city with the maximum avg course marks.
  > **Example Output:**
  > ```text
  > Mumbai
  > ```
