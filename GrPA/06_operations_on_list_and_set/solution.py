def list_mutating_operations(items: list, item1, item2):
    """Example Input:
list_mutating_operations(["Apple", "Cherry","Banana","Grapes"], "Blueberry","Apple")

Expected Output:
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
(['Cherry', 'Blueberry', None], 'Grapes')"""
    pass

def list_non_mutating_operations(items: list, item1, item2):
    """Example Input:
list_non_mutating_operations(["Apple","Cherry","Banana", "Grapes", 'Orange', 'Pineapple'], "Blueberry","Apple")

Expected Output:
sorted: ['Apple', 'Banana', 'Cherry', 'Grapes', 'Orange', 'Pineapple']
append: ['Apple', 'Cherry', 'Banana', 'Grapes', 'Orange', 'Pineapple', 'Blueberry']
insert: ['Apple', 'Cherry', 'Banana', 'Apple', 'Grapes', 'Orange', 'Pineapple']
extend: ['Apple', 'Cherry', 'Banana', 'Grapes', 'Orange', 'Pineapple', 'Apple', 'Cherry', 'Banana']
pop: ['Apple', 'Cherry', 'Banana', 'Grapes', 'Pineapple']
remove: ['Cherry', 'Banana', 'Grapes', 'Orange', 'Pineapple']
modify_index: ['Apple', 'Cherry', 'Banana', None, 'Orange', 'Pineapple']
modify_slice: [None, 'Cherry', None, 'Grapes', None, 'Pineapple']
delete_slice: ['Cherry', 'Grapes', 'Pineapple']
['Apple', 'Cherry', 'Banana', 'Grapes', 'Orange', 'Pineapple']"""
    pass

def do_set_operation(set1, set2, set3, item1, item2):
    """Example Input:
do_set_operation({1,2,3,4}, {3,4,5,6}, {1,2,5,6,7,8}, 5, 3)

Expected Output:
[1, 2, 3, 4, 5]
[1, 2, 4, 5]
[1, 2, 3, 4, 5, 6]
[3, 4]
[5, 6]
[1, 2, 3, 4, 5, 6, 7, 8]
[3, 4]
[1, 2, 3, 4, 7, 8]
([3, 4], [3, 4, 5, 6], [1, 2, 5, 6, 7, 8])"""
    pass