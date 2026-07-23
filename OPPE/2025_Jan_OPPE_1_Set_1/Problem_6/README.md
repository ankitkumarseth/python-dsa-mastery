# Student Score Filter

Given the data of student scores in a dictionary where keys are student names and values are lists of scores, write a function `filter_students` to filter student roll names based on the following criteria:

- `'excellent'`: Students with average score >= 85.
- `'good'`: Students with average score between 50(inclusive) and 85(exclusive).
- `'all_pass'`: Students with all scores >= 50.
- `'balanced'`: Students whose difference between max score and min score is <= 10.

**NOTE:** This is a function type question, you don't have to take input or print the output, just have to complete the required function definition. You can define helper functions if needed, but the actual solution should be in the given function template.

### Example

```python
data = {
    "Alice": [90, 80, 85],
    "Bob": [40, 50, 60],
    "Charlie": [30, 40, 20], 
    "Ram": [78, 92, 85, 79, 81],
    "Babu": [67, 70, 75],
    "Kumar": [ 100, 100, 100, 100, 100, 100, 40]
}
```
- `filter_students(data, 'excellent')` -> `{'Alice', 'Kumar'}`
- `filter_students(data, 'good')` -> `{'Babu', 'Bob', 'Ram'}`
- `filter_students(data, 'all_pass')` -> `{'Alice', 'Babu', 'Ram'}`
- `filter_students(data, 'balanced')` -> `{'Alice', 'Babu'}`
