int_iterable = range(1, 10, 3)
string_iterable = ['Apple', 'Orange', 'Banana']
some_value = 4
some_collection = [1, 2, 3]
some_iterable = (1, 2, 3)
another_iterable = {'apple', 'banana', 'cherry'}
yet_another_iterable = range(1, 10)
empty_list = []
empty_set = set()
empty_tuple = tuple()
singleton_list = [1]
singleton_set = {1}
singleton_tuple = (1,)
a_falsy_list = []
a_falsy_set = set()
a_truthy_tuple = (1,)
int_iterable_min = min(int_iterable)
int_iterable_max = max(int_iterable)
int_iterable_sum = sum(int_iterable)
int_iterable_len = len(int_iterable)
int_iterable_sorted = sorted(int_iterable)
int_iterable_sorted_desc = sorted(int_iterable, reverse=True)
if hasattr(int_iterable, '__reversed__'):
    int_iterable_reversed = list(reversed(int_iterable))
else:
    int_iterable_reversed = list(int_iterable_sorted_desc)
if hasattr(some_collection, '__getitem__'):
    third_last_element = some_collection[-3]
else:
    third_last_element = None
if hasattr(some_collection, '__getitem__') and hasattr(some_collection, '__len__'):
    odd_index_elements = some_collection[1::2]
else:
    odd_index_elements = None
is_some_value_in_some_collection = some_value in some_collection
if hasattr(some_collection, '__getitem__'):
    is_some_value_in_even_indices = some_value in some_collection[::2]
else:
    is_some_value_in_even_indices = None
all_iterables = list(some_iterable) + list(another_iterable) + list(yet_another_iterable)
if hasattr(string_iterable, '__getitem__'):
    all_concat = '-'.join(string_iterable)
else:
    all_concat = '-'.join(sorted(string_iterable))