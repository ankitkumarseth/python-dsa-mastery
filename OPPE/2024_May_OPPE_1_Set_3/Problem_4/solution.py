import sys

def solve(input_data=None):
    '''
    Read from input_data if provided (for testing), else from sys.stdin.
    Print the output according to the problem.
    '''
    if input_data is None:
        input_data = sys.stdin.read()

    # Write your code here
    lines = input_data.splitlines()
    get_input = iter(lines)
    num_of_days = next(get_input)
    initial_balance = int(next(get_input))
    current_balance = initial_balance
    for line in get_input:
        transactions = [int(transaction) for transaction in line.split()]
        daily_balances = []
        for transaction in transactions:
            current_balance += transaction
            daily_balances.append(current_balance)
        print(f'{min(daily_balances)},{max(daily_balances)},{current_balance}')



if __name__ == '__main__':
    solve()
