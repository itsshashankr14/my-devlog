# Given an array and two disjoint sets A (liked) and B (disliked),
# compute the total happiness where:
# +1 is added for each element in A, -1 is subtracted for each in B.

n, m = map(int,input().split())
arr = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))

happiness = 0

for i in arr:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
print(happiness)