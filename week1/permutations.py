# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

s ,k =input().split()
k = int(k)

perm = permutations(sorted(s),k)

for p in perm:
    print(''.join(p))

""" Explanation:
sorted(s) ensures the characters are sorted lexicographically.

permutations(..., k) gives all k-length permutations.

''.join(p) converts tuple to string before printing."""