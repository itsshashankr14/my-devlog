# Given two integers a and b, perform and print:
# 1. The result of integer division a // b
# 2. The result of the modulo operation a % b
# 3. The result of divmod(a, b), which returns a tuple (a // b, a % b)

# Read two integers from input
a = int(input())
b = int(input())

# Print integer division
print(a // b)

# Print remainder (modulo)
print(a % b)

# Print tuple (quotient, remainder) using divmod
print(divmod(a, b))
