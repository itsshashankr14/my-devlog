# Task: Perform a sequence of set operations (pop, remove, discard) on a set of integers.
# Input:
#   Line 1: n - size of the set
#   Line 2: n space-separated integers
#   Line 3: N - number of commands
#   Next N lines: commands like pop, remove x, discard x
# Output:
#   Print the sum of the final set after all operations

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))
    else:
        raise ValueError("Unknown command")
        exit(0)

print(sum(s))