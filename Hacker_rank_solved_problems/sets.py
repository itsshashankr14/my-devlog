# Given a list of plant heights (with possible duplicates),
# compute the average of all **distinct** heights.
# Use sets to remove duplicates and print the result rounded to 3 decimal places.

def average(array):
    distinct_heights = set(array)
    return round(sum(distinct_heights) / len(distinct_heights),3)

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    result = average(arr)
    print(result)