def can_stack(cubes):
    top = float('inf')  # Start with infinite height
    while cubes:
        if cubes[0] >= cubes[-1] and cubes[0] <= top:
            top = cubes.pop(0)
        elif cubes[-1] >= cubes[0] and cubes[-1] <= top:
            top = cubes.pop()
        else:
            return "No"
    return "Yes"

# Read input
T = int(input())
for _ in range(T):
    n = int(input())
    cubes = list(map(int, input().split()))
    print(can_stack(cubes))
