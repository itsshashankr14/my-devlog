# defaultdict group index lookup problem using Python:

from collections import defaultdict

# Input values for group sizes
n, m = map(int, input().split())

# Create a defaultdict to store positions of words in group A
group_a = defaultdict(list)

# Read group A words and store their positions (1-indexed)
for i in range(1, n + 1):
    word = input()
    group_a[word].append(i)

# Read group B words and check their positions in group A
for _ in range(m):
    query = input()
    if query in group_a:
        print(' '.join(map(str, group_a[query])))
    else:
        print(-1)
