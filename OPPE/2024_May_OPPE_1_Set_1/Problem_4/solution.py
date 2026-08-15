import sys
from collections import Counter


def solve(input_data=None):
    '''
    Read from input_data if provided (for testing), else from sys.stdin.
    Print the RLE sequence for each line.
    '''
    if input_data is None:
        input_data = sys.stdin.read()

    # Write your code here
    lines = input_data.strip().split('\n')
    get_input = iter(lines)
    num_items = int(next(get_input))

    for num in get_input:
        counts = Counter(num)
        num_count = counts.most_common()
        output = ' '.join(f"{count} {digit}" for digit, count in num_count)
        print(output)

if __name__ == '__main__':
    solve()