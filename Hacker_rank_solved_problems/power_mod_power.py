# Given three integers a, b, and m:
# Print pow(a, b) on the first line
# Print pow(a, b, m) on the second line (i.e., (a^b) % m using built-in modular exponentiation)

a = int(input())
b = int(input())
m = int(input())

print(pow(a,b))
print(pow(a, b, m))