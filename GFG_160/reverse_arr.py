class solution:
    def reverse_arrr(self, arr):
        n = len(arr)
        right = n - 1
        left = 0
        while left < right :
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

arr = [1, 2, 3, 4, 5]
sl = solution()
sl.reverse_arrr(arr)
print(arr)

