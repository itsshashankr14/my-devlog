# Enter your code here. Read input from STDIN. Print output to STDOUT
#collections.Counter()
#A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.


from collections import Counter

X = int(input())

shoe_sizes = Counter(map(int,input().split()))

N = int(input())

earnings = 0

for _ in range(N):
    size, price = map(int, input().split())
    if shoe_sizes[size] > 0:
        earnings += price
        shoe_sizes[size] -= 1
        
print(earnings)