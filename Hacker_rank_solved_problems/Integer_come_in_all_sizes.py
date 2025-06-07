# Given four integers a, b, c, and d, compute and print the value of (a^b) + (c^d).
# Python can handle arbitrarily large integers, so no overflow concerns.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

result = pow(a, b) + pow(c, d)
print(result)