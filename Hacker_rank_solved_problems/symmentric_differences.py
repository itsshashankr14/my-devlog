# Given two sets of integers, print the symmetric difference in ascending order.
# Symmetric difference: elements in either set, but not in both.

m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
#symmetric_difference = a.symmetric_difference(b)

for num in sorted( a^b ):
    print(num)