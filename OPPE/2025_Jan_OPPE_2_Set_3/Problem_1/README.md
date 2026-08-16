# Extract Border Elements from a List

Write a function `extract_border_elements` that takes a list of integers as input and returns a new list containing only the first and last elements if the list has more than one element.

- If the list has only one element, return it as a single-element list.
- If the list is empty, return an empty list.

NOTE: This is a function type question, you don't have to take input or print the output, just complete the required function definition.

### Example
- `extract_border_elements([1, 2, 3, 4])` → `[1, 4]`
- `extract_border_elements([5])` → `[5]`
- `extract_border_elements([])` → `[]`
- `extract_border_elements([7, 8, 9, 10, 11])` → `[7, 11]`
