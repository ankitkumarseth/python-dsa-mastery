import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_transfer_amount():
    accounts1 = {'12345': 500, '67890': 1000, '98764': 1500}
    solution.transfer_amount(accounts1, '12345', '67890', 1000)
    assert accounts1 == {'12345': 500, '67890': 1000, '98764': 1500}

    solution.transfer_amount(accounts1, '12345', '67890', 200)
    assert accounts1 == {'12345': 300, '67890': 1200, '98764': 1500}

    accounts2 = {'12345': 500, '67890': 1000, '98764': 1500}
    solution.transfer_amount(accounts2, '12345', '67890', 400)
    assert accounts2 == {'12345': 100, '67890': 1400, '98764': 1500}

    accounts3 = {'12345': 100, '67890': 1400, '98764': 1500}
    solution.transfer_amount(accounts3, '98764', '67890', 1500)
    assert accounts3 == {'12345': 100, '67890': 2900, '98764': 0}

    accounts4 = {'12345': 100, '67890': 1400, '98764': 1500}
    solution.transfer_amount(accounts4, '98764', '67890', -1500)
    assert accounts4 == {'12345': 100, '67890': 1400, '98764': 1500}

    accounts5 = {'12345': 100, '67890': 1400, '98764': 1500}
    solution.transfer_amount(accounts5, '98764', '20348', 1500)
    assert accounts5 == {'12345': 100, '67890': 1400, '98764': 1500}

    solution.transfer_amount(accounts5, '20348', '98764', 1500)
    assert accounts5 == {'12345': 100, '67890': 1400, '98764': 1500}

    solution.transfer_amount(accounts5, '12345', '98764', 50)
    assert accounts5 == {'12345': 50, '67890': 1400, '98764': 1550}
