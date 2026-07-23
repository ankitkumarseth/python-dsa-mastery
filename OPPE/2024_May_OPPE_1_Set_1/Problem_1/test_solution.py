import os, pytest, importlib.util
SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_abs_diff():
    assert solution.abs_diff_between_sum_and_sum_of_squares(1,2) == 2
    assert solution.abs_diff_between_sum_and_sum_of_squares(-1,2) == 4
    assert solution.abs_diff_between_sum_and_sum_of_squares(2,3) == 8

def test_swap_except_middle_three():
    assert solution.swap_except_middle_three("firstabclast1") == "last1abcfirst"
    assert solution.swap_except_middle_three("abcdefghi") == "ghidefabc"

def test_interleave_lists():
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    list3 = ['one', 'two', 'three']
    assert solution.interleave_lists(list1,list2,list3) == [1, 'a', 'one', 2, 'b', 'two', 3, 'c', 'three']

def test_has_more_than_5_unique_digits():
    assert solution.has_more_than_5_unique_digits(11223344445) is False
    assert solution.has_more_than_5_unique_digits(11222233344445555666) is True

def test_final_position():
    assert solution.final_position((1,1), (2,2), 3) == (7,7)
    assert solution.final_position((1,2), (2,1), 3) == (7,5)

def test_remove_keys_not_in_list():
    d = {1:'a',2:'b',3:'c',4:'d',5:'e'}
    l = [7,6,5,4,3]
    solution.remove_keys_not_in_list(d, l)
    assert d == {3:'c',4:'d',5:'e'}
