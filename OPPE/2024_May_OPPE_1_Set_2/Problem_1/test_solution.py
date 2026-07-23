import os, importlib.util
SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_triangle():
    assert solution.is_right_triangle_with_even_sides(3, 3, 5) == False
    assert solution.is_right_triangle_with_even_sides(6, 8, 10) == True
    assert solution.is_right_triangle_with_even_sides(3, 4, 5) == False

def test_indices():
    assert solution.is_odd_indices_alpha_and_even_indices_digits("a1b2c3") == False
    assert solution.is_odd_indices_alpha_and_even_indices_digits("1a2b3c") == True
    assert solution.is_odd_indices_alpha_and_even_indices_digits("3x4b6d") == True
    assert solution.is_odd_indices_alpha_and_even_indices_digits("123abc") == False

def test_swap():
    l = [1, 2, 3, 4, 5, 6]
    solution.swap_even_and_odd_indices(l)
    assert l == [2, 1, 4, 3, 6, 5]

    l2 = [10, 20, 30, 40]
    solution.swap_even_and_odd_indices(l2)
    assert l2 == [20, 10, 40, 30]

def test_unique():
    assert solution.unique_chars_present_in_first_not_in_second("water", "watch") == {'e','r'}
    assert solution.unique_chars_present_in_first_not_in_second("python", "pattern") == {'h','o','y'}

def test_repeat():
    assert solution.repeat((2, 3)) == (2, 2, 2, 3, 3)
    assert solution.repeat((4, 1)) == (4, 1, 1, 1, 1)

def test_squares():
    assert solution.num_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    assert solution.num_squares(3) == {1: 1, 2: 4, 3: 9}
