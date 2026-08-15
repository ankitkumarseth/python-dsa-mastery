# Problem 3

Given a dictionary of student roll numbers with the list of courses they chose, find the courses sorted from the most number of enrollments to the least.

### Example Input
```python
student_courses = {
    '101': ['Math', 'Science'],
    '102': ['Math'],
    '103': ['Science', 'Math'],
    '104': ['Math', 'History'],
    '105': ['English', 'History', 'Science']
}
```

### Example Output
```python
['Math', 'Science', 'History', 'English']
```

### Explanation
- **Math**: 4 enrollments
- **Science**: 3 enrollments
- **History**: 2 enrollments
- **English**: 1 enrollment
