import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_add_middle_elems_to_ends_in_even_length_tuple():
    assert solution.add_middle_elems_to_ends_in_even_length_tuple((10, 20, 30, 40, 50, 60)) == (30, 10, 20, 50, 60, 40)
    assert solution.add_middle_elems_to_ends_in_even_length_tuple(("Lenovo", "Dell", "HP", "Asus", "Mac" , "Thinkpad")) == ('HP', 'Lenovo', 'Dell', 'Mac', 'Thinkpad', 'Asus')
    assert solution.add_middle_elems_to_ends_in_even_length_tuple((5, 15, 25, 35)) == (15, 5, 35, 25)
    assert solution.add_middle_elems_to_ends_in_even_length_tuple(("Apple", "Microsoft", "Google", "Amazon")) == ('Microsoft', 'Apple', 'Amazon', 'Google')
    # Edge case: tuple of length 2
    assert solution.add_middle_elems_to_ends_in_even_length_tuple((1, 2)) == (1, 2)
