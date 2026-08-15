import sys

def solve(input_data=None):
    '''
    Read from input_data if provided (for testing), else from sys.stdin.
    Print the RLE sequence for each line.
    '''
    if input_data is None:
        input_data = sys.stdin.read()

    # Write your code here
    lines = input_data.strip().lower().split('\n')
    get_input = iter(lines)
    count = next(get_input)

    for line in get_input:
        words = line.split(',')
        max_streak = 1
        current_streak = 1
        
        # Use the zip trick we just talked about to compare adjacent words!
        for curr, nxt in zip(words, words[1:]):
            if curr[-1] == nxt[0]:
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                current_streak = 1
                
        print(max_streak)

if __name__ == '__main__':
    solve()
