# Student Marks Filter

Given the data of student marks in the format of list of tuples of format `(rollno:str, marks:int)`, write a function to filter student roll numbers based on the following criteria:
- `'above_average'`: Students with marks above or equal to the average.
- `'below_average'`: Students with marks below the average.
- `'fail'`: Students with marks less than 40.
- `'toppers'`: Students with marks 90 or above.
- `None`: Return all roll numbers.
- Any other value should return `None`.

The order of the roll numbers in the filtered roll numbers should be same as they appear in the data.

NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition. You can define helper functions if needed, but the actual solution should be in the given function template.

### Examples
**Input:**
```
data = [("101", 85), ("102", 75), ("103", 45), ("104", 95), ("105", 35)]
criteria = 'above_average'
```
**Output:**
```
["101", "102", "104"]
```

**Input:**
```
data = [("101", 85), ("102", 75), ("103", 45), ("104", 95), ("105", 35)]
criteria = 'fail'
```
**Output:**
```
["105"]
```

**Input:**
```
data = [("101", 85), ("102", 75), ("103", 45), ("104", 95), ("105", 35)]
criteria = 'toppers'
```
**Output:**
```
["104"]
```

**Input:**
```
data = [("101", 85), ("102", 75), ("103", 45), ("104", 95), ("105", 35)]
criteria = None
```
**Output:**
```
["101", "102", "103", "104", "105"]
```
