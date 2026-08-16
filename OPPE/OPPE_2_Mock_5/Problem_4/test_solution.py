import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_calculate_total_spent():
    file1 = os.path.join(os.path.dirname(__file__), 'test_input_1.txt')
    expected_output_1 = {'Alice Brown': 141.97, 'Bob Johnson': 289.43, 'Carol White': 806.52, 'John Doe': 569.09}
    
    # We round the values to 2 decimal places to avoid floating point precision issues in test assertion
    result_1 = solution.calculate_total_spent(file1)
    result_1_rounded = {k: round(v, 2) for k, v in result_1.items()} if result_1 else None
    assert result_1_rounded == expected_output_1

    file2 = os.path.join(os.path.dirname(__file__), 'test_input_2.txt')
    expected_output_2 = {'Alice Brown': 928.26, 'Carol White': 369.05, 'Jane Smith': 32.4, 'John Doe': 852.81}
    
    result_2 = solution.calculate_total_spent(file2)
    result_2_rounded = {k: round(v, 2) for k, v in result_2.items()} if result_2 else None
    assert result_2_rounded == expected_output_2
