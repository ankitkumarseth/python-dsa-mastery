import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_count_strings_length_divisible_by_3_or_5():
    assert solution.count_strings_length_divisible_by_3_or_5(["123456789", "123456789123", "1234567"]) == 2
    assert solution.count_strings_length_divisible_by_3_or_5(["disproportionately", "misinterpretation", "contradictory"]) == 1
    assert solution.count_strings_length_divisible_by_3_or_5(["clarification", "misconception", "identificationn"]) == 1
    assert solution.count_strings_length_divisible_by_3_or_5(["revolutionary", "contradictory", "justification"]) == 0
    assert solution.count_strings_length_divisible_by_3_or_5(["disproportionate", "misinterpretatn", "acknowledgement"]) == 2
    # Edge case: Empty list
    assert solution.count_strings_length_divisible_by_3_or_5([]) == 0
    # Edge case: Empty string (length 0, divisible by 3 and 5)
    assert solution.count_strings_length_divisible_by_3_or_5([""]) == 1
