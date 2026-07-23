import sys

def solve():
    # Read from file if sys.argv[1] is provided, else from stdin
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            content = f.read()
    else:
        content = sys.stdin.read()
        
    # Write your logic here
    ...

if __name__ == '__main__':
    solve()
