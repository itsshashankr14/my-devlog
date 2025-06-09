# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

s,k = input().split()
k=int(k)

s=sorted(s)

for i in range(1,k+1):
    for combo in combinations(s,i):
        print(''.join(combo))


"""Explanation:
sorted(s) ensures characters are ordered alphabetically.

Loop through lengths from 1 to k.

combinations(s, i) generates all i-length combinations.

''.join(combo) converts tuple to string before printing.
"""