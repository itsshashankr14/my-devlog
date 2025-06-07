# Print a palindromic triangle of size n using exactly one print statement inside the given for-loop.
# No strings or multiple for-loops allowed.

for i in range(1, int(input()) + 1):
    print(int((10 ** i - 1) // 9) ** 2)
