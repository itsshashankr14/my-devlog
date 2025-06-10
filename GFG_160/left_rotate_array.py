def left_rotate(arr, d):
    n = len(arr)
    d %= n
    def reverse(start, end):
        while start < end :
            arr[start],arr[end] = arr[end],arr[start]
            start += 1
            end -= 1

    reverse(0, d - 1)
    reverse(d, n - 1)
    reverse(0, n - 1)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 3
    left_rotate(arr, d)
    print("Array after left rotation:", arr)  # Output: [3, 4, 5, 6, 7, 1, 2]
