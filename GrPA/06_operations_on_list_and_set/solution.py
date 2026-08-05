def list_mutating_operations(items:list, item1, item2):
    """
    Example Input:
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
    (['Cherry', 'Blueberry', None], 'Grapes')
    """
    # sort the `items` inplace
    items.sort()
    print("sorted:",items)

    # add item1 to the `items` at the end
    items.append(item1)
    print("append:",items)

    # add item2 at index 3
    items.insert(3, item2)
    print("insert:",items)

    # extend `items` with the first three elements in `items`
    items.extend(items[:3])
    print("extend:", items)

    # pop the fifth element and store it in variable `popped_item`
    popped_item = items.pop(4)
    print("pop:",items)

    # remove first occurance of `item2` from the list
    items.remove(item2)
    print("remove:",items)

    # make the element at index 4 None
    items[4] = None
    print("modify_index:",items)

    # make the even indices None
    items[::2] = [None] * len(items[::2])
    print("modify_slice:",items)

    # delete the third last element
    del items[-3]
    print("delete_index:",items)

    # delete the even indices
    del items[::2]
    print("delete_slice:",items)

    return items, popped_item

def list_non_mutating_operations(items:list, item1, item2):
    """
    Example Input:
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
    ['Apple', 'Cherry', 'Banana', 'Grapes', 'Orange', 'Pineapple']
    """
    # print the sorted version of items
    print("sorted:", sorted(items))

    # print a list with item1 appended to the `items` at the end
    print("append:", items + [item1])

    # print a list with item2 added to items at index 3
    print("insert:", items[:3] + [item2] + items[3:])

    # print a list with the first three elements in `items` added to the end of the `items` again
    print("extend:", items + items[:3])

    #  print a list with the fifth element from `items` removed
    print("pop:", items[:4] + items[5:])

    # print a list with first occurance of `item2` removed from `items`
    print("remove:", items[:items.index(item2)] + items[items.index(item2) + 1 :])

    # print a list with the fourth element of `items` changed to None
    print("modify_index:", items[:3] + [None] + items[4:])

    # print a list with the even indices changed to None
    print("modify_slice:", [None if i % 2 == 0 else x for i, x in enumerate(items)])

    # print a list with the even indices removed
    print("delete_slice:", items[1::2])

    return items

def do_set_operation(set1, set2, set3, item1, item2):
    """
    Example Input:
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
    ([3, 4], [3, 4, 5, 6], [1, 2, 5, 6, 7, 8])
    """
    # add item1 to set1
    set1.add(item1)
    print(sorted(set1))
    # remove item2 from set1. What if item2 is not in set1?
    set1.discard(item2)
    print(sorted(set1))

    # add elements from set2 to set1
    set1.update(set2)
    print(sorted(set1))

    # remove all elements from set1 that are in set3
    set1.difference_update(set3)
    print(sorted(set1))

    # print the common elements in both set2 and set3 as a sorted list.
    print(sorted(set2 & set3))

    # print all unique elements present in set1, set2 an set3 as a sorted list
    print(sorted(set1 | set2 | set3))

    # print all unique elements that are in set2 but not in set3 as a sorted list
    print(sorted(set2 - set3))

    # print all the non common elements from both set2 and set3
    print(sorted(set2 ^ set3))

    return set1,sorted(set1),sorted(set2),sorted(set3)
