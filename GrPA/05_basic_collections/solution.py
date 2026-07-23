# The values of the below variables will be changed by the evaluator
int_iterable = range(1,10,3)
string_iterable = ["Apple","Orange", "Banana"]
some_value = 4
some_collection = [1,2,3] # list | set | tuple

some_iterable = (1,2,3)
another_iterable = {"apple", "banana", "cherry"} # can be any iterable
yet_another_iterable = range(1,10)

# --- STUDENT CODE BEGINS ---
empty_list = ...
empty_set = ... # be carefull here you might end up creating something called as an empty dict
empty_tuple = ...

singleton_list = ... # list: A list with only one element
singleton_set = ... # set: A set with only one element
singleton_tuple = ... # tuple: A tuple with only one element

a_falsy_list = ... # list: a list but when passed to bool function should return False.
a_falsy_set = ... # set: a set but when passed to bool function should return False.
a_truthy_tuple = ... # tuple: a tuple but when passed to bool function should return True

int_iterable_min = ... # int: find the minimum of int_iterable. Hint: use min function
int_iterable_max = ... # int: find the maximum of int_iterable. Hint: use max function
int_iterable_sum = ... # int: you know what to do
int_iterable_len = ... # int: really... you need hint?
int_iterable_sorted = ... # list: the int_iterable sorted in ascending order
int_iterable_sorted_desc = ... # list: the int_iterable sorted in desc order

if hasattr(int_iterable, "__reversed__"): # some iterables are not reversible why?
    int_iterable_reversed = ... # list: the int_iterable reversed use the reversed function
else: # in that case sort it in ascending order and reverse it
    int_iterable_reversed = ... #list

if hasattr(some_collection, '__getitem__'): # some collections are not indexable why?
    third_last_element = ... # the third last element of `some_collection`
else: # in that case set third_last_element to None
    third_last_element = ...

if hasattr(some_collection, '__getitem__') and hasattr(some_collection, '__len__'): # some collections are not slicable
    odd_index_elements = ... # type(some_collection): the elements at odd indices of `some_collection`
else: # in that case set odd_index_elements to None
    odd_index_elements = ...

is_some_value_in_some_collection = ... # bool: True if `some_value` is present in `some_collection`

if hasattr(some_collection, '__getitem__'): # some collections are not ordered
    is_some_value_in_even_indices = ... # bool: True if `some_value` is present in even indices of `some_collection`
else: # in that case set is_some_value_in_even_indices to None
    is_some_value_in_even_indices = ...

all_iterables = ... # list: concatenate `some_iterable`, `another_iterable` and `yet_another_iterable` into a list.

if hasattr(string_iterable, '__getitem__') : # some iterables are not ordered
    all_concat = ... # str: concatenate all the strings in string_iterable with '-' in between
else: # in that case sort them and concatenate
    all_concat = ...
