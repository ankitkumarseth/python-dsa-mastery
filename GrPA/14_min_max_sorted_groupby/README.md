# GrPA Min, Max, Sorted, Groupby

Implement all the given functions below according to the docstrings.

> [!WARNING]
> **Note:** For specific functions (`min_course_marks`, `max_course_marks`, `rollno_of_max_marks`, `sort_rollno_by_marks`, `count_students_by_cities`, `city_with_max_no_of_students`, `group_rollnos_by_cities`, `city_with_max_avg_course_mark`), you are **not** allowed to use `if` statements, `for`/`while` loops, or comprehensions! You must compose your logic using `min`, `max`, `sorted`, and your `groupby` / `apply_to_groups` helper functions.

### Student Data Schema
The following functions (from `min_course_marks` onwards) will receive `student_data`, which is a list of dictionaries structured like this:
```python
student_data = [
    {"rollno": 1, "city": "Chennai", "marks": {"CT": 80, "Math-1": 90, "Stats-1": 85}},
    {"rollno": 2, "city": "Mumbai", "marks": {"CT": 90, "Math-1": 80, "Stats-1": 90}},
    {"rollno": 3, "city": "Mumbai", "marks": {"CT": 85, "Math-1": 85, "Stats-1": 85}},
    {"rollno": 4, "city": "Delhi", "marks": {"CT": 70, "Math-1": 70, "Stats-1": 70}}
]
```

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
### Examples
**Input:**
```python
min_course_marks(student_data, "CT")
```
**Output:**
```text
70
```

* **`max_course_marks(student_data: list, course: str) -> int`**: Return the max marks on a given course.
### Examples
**Input:**
```python
max_course_marks(student_data, "Math-1")
```
**Output:**
```text
90
```

* **`rollno_of_max_marks(student_data: list, course: str) -> int`**: Return the rollno of student with max marks in a course.
### Examples
**Input:**
```python
rollno_of_max_marks(student_data, "Stats-1")
```
**Output:**
```text
2
```

* **`sort_rollno_by_marks(student_data: list, course1: str, course2: str, course3: str) -> list`**: Return a sorted list of rollno sorted based on their marks on the three course marks. `course1` is compared first, then `course2`, then `course3` to break ties. (Hint: use tuples comparison).
### Examples
**Input:**
```python
sort_rollno_by_marks(student_data, "CT", "Math-1", "Stats-1")
```
**Output:**
```python
[4, 1, 3, 2]
```

* **`count_students_by_cities(student_data: list) -> dict`**: Create a dictionary with city as key and number of students from each city as value.
### Examples
**Input:**
```python
count_students_by_cities(student_data)
```
**Output:**
```python
{'Chennai': 1, 'Mumbai': 2, 'Delhi': 1}
```

* **`city_with_max_no_of_students(student_data: list) -> str`**: Find the city with the maximum number of students.
### Examples
**Input:**
```python
city_with_max_no_of_students(student_data)
```
**Output:**
```text
Mumbai
```

* **`group_rollnos_by_cities(student_data: list) -> dict`**: Create a dictionary with city as key and a sorted list of rollno of students that belong to that city as the value.
### Examples
**Input:**
```python
group_rollnos_by_cities(student_data)
```
**Output:**
```python
{'Chennai': [1], 'Mumbai': [2, 3], 'Delhi': [4]}
```

* **`city_with_max_avg_course_mark(student_data: list, course: str) -> str`**: Find the city with the maximum avg course marks.
### Examples
**Input:**
```python
city_with_max_avg_course_mark(student_data, "CT")
```
**Output:**
```text
Mumbai
```
