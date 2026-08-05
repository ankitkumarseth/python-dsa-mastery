from collections import defaultdict

def groupby(data: list, key: callable):
    """Given a list of items, and a key, create a dictionary with the key as key function called
on item and the list of items with the same key as the corresponding value.
The order of items in the group should be the same order in the original list.

Example Input:
groupby(["Apple", "Banana", "Avocado", "Amla", "Black berry", "Blue berry"], lambda x: x[0])

Expected Output:
{'A': ['Apple', 'Avocado', 'Amla'], 'B': ['Banana', 'Black berry', 'Blue berry']}"""
    pass

def apply_to_groups(groups: dict, func: callable):
    """Apply a function to the list of items for each group.

Example Input:
apply_to_groups({"A": ["Apple", "Avocado"], "B": ["Banana", "Black berry"]}, len)

Expected Output:
{'A': 2, 'B': 2}"""
    pass

def min_course_marks(student_data, course):
    """Return the min marks on a given course

Example Input:
min_course_marks(student_data, "CT")

Expected Output:
70"""
    pass

def max_course_marks(student_data, course):
    """Return the max marks on a given course

Example Input:
max_course_marks(student_data, "Math-1")

Expected Output:
90"""
    pass

def rollno_of_max_marks(student_data, course):
    """Return the rollno of student with max marks in a course

Example Input:
rollno_of_max_marks(student_data, "Stats-1")

Expected Output:
2"""
    pass

def sort_rollno_by_marks(student_data, course1, course2, course3):
    """Return a sorted list of rollno sorted based on their marks on the three course marks.
course1 is compared first, then course2, then course3 to break ties.
Hint: use tuples comparision

Example Input:
sort_rollno_by_marks(student_data, "CT", "Math-1", "Stats-1")

Expected Output:
[4, 1, 3, 2]"""
    pass

def count_students_by_cities(student_data):
    """Create a dictionary with city as key and number of students from each city as value.

Example Input:
count_students_by_cities(student_data)

Expected Output:
{'Chennai': 1, 'Mumbai': 2, 'Delhi': 1}"""
    pass

def city_with_max_no_of_students(student_data):
    """Find the city with the maximum number of students.

Example Input:
city_with_max_no_of_students(student_data)

Expected Output:
'Mumbai'"""
    pass

def group_rollnos_by_cities(student_data):
    """Create a dictionary with city as key and
a sorted list of rollno of students that belong to
that city as the value.

Example Input:
group_rollnos_by_cities(student_data)

Expected Output:
{'Chennai': [1], 'Mumbai': [2, 3], 'Delhi': [4]}"""
    pass

def city_with_max_avg_course_mark(student_data, course):
    """Find the city with the maximum avg course marks.

Example Input:
city_with_max_avg_course_mark(student_data, "CT")

Expected Output:
'Mumbai'"""
    pass