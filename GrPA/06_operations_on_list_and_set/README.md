# GrPA Operations on List and Set

This exercise covers common operations you can perform on `list` and `set` collections in Python.

### Tasks
You need to complete three functions:

* **`list_mutating_operations(items: list, item1, item2)`**: Learn the list methods and operations that will modify the list **in-place**. Note that you should not be creating a new list anywhere in this function.
### Examples
**Input:**
```python
list_mutating_operations(["Apple", "Cherry","Banana","Grapes"], "Blueberry","Apple")
```
**Output:**
```text
sorted: ['Apple', 'Banana', 'Cherry', 'Grapes']
append: ['Apple', 'Banana', 'Cherry', 'Grapes', 'Blueberry']
insert: ['Apple', 'Banana', 'Cherry', 'Apple', 'Grapes', 'Blueberry']
extend: ['Apple', 'Banana', 'Cherry', 'Apple', 'Grapes', 'Blueberry', 'Apple', 'Banana', 'Cherry']
pop: ['Apple', 'Banana', 'Cherry', 'Apple', 'Blueberry', 'Apple', 'Banana', 'Cherry']
remove: ['Banana', 'Cherry', 'Apple', 'Blueberry', 'Apple', 'Banana', 'Cherry']
modify_index: ['Banana', 'Cherry', 'Apple', 'Blueberry', None, 'Banana', 'Cherry']
modify_slice: [None, 'Cherry', None, 'Blueberry', None, 'Banana', None]
delete_index: [None, 'Cherry', None, 'Blueberry', 'Banana', None]
delete_slice: ['Cherry', 'Blueberry', None]
(['Cherry', 'Blueberry', None], 'Grapes')
```

* **`list_non_mutating_operations(items: list, item1, item2)`**: Learn how to create new lists that resemble the result of operations, but do **not affect** the original list.
### Examples
**Input:**
```python
list_non_mutating_operations(["Apple","Cherry","Banana", "Grapes", 'Orange', 'Pineapple'], "Blueberry","Apple")
```
**Output:**
```text
sorted: ['Apple', 'Banana', 'Cherry', 'Grapes', 'Orange', 'Pineapple']
append: ['Apple', 'Cherry', 'Banana', 'Grapes', 'Orange', 'Pineapple', 'Blueberry']
insert: ['Apple', 'Cherry', 'Banana', 'Apple', 'Grapes', 'Orange', 'Pineapple']
extend: ['Apple', 'Cherry', 'Banana', 'Grapes', 'Orange', 'Pineapple', 'Apple', 'Cherry', 'Banana']
pop: ['Apple', 'Cherry', 'Banana', 'Grapes', 'Pineapple']
remove: ['Cherry', 'Banana', 'Grapes', 'Orange', 'Pineapple']
modify_index: ['Apple', 'Cherry', 'Banana', None, 'Orange', 'Pineapple']
modify_slice: [None, 'Cherry', None, 'Grapes', None, 'Pineapple']
delete_slice: ['Cherry', 'Grapes', 'Pineapple']
['Apple', 'Cherry', 'Banana', 'Grapes', 'Orange', 'Pineapple']
```

* **`do_set_operation(set1, set2, set3, item1, item2)`**: Learn various operations that you can perform with sets (unions, intersections, differences, etc.).
### Examples
**Input:**
```python
do_set_operation({1,2,3,4}, {3,4,5,6}, {1,2,5,6,7,8}, 5, 3)
```
**Output:**
```text
[1, 2, 3, 4, 5]
[1, 2, 4, 5]
[1, 2, 3, 4, 5, 6]
[3, 4]
[5, 6]
[1, 2, 3, 4, 5, 6, 7, 8]
[3, 4]
[1, 2, 3, 4, 7, 8]
([3, 4], [3, 4, 5, 6], [1, 2, 5, 6, 7, 8])
```

> [!WARNING]
> **NOTE:** You should not use `for` loop, `while` loop, or the words `for` and `while` anywhere in this exercise!
