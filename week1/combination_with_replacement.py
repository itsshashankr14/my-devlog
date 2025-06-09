# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

s,k = input().split()
k=int(k)
s = sorted(s)

for combo in combinations_with_replacement(s,k):
    print(''.join(combo))


"""🔍 Explanation:
sorted(s) ensures the combinations are in lexicographic order.

combinations_with_replacement(s, k) allows repeating characters.

We join each tuple to make it a string before printing."""