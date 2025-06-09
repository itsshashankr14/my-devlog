# Check if all integers in a list are positive and
# if at least one is a palindrome.
# Return True only if both conditions are satisfied.

n, nums = int(input()), input().split()
print(all(int(x) > 0 for x in nums) and any(x == x[::-1] for x in nums))
