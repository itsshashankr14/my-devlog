# Task: Move all 0s to the end of the array in-place.
#       Preserve the order of non-zero elements.
# Constraint: No extra array should be used (in-place operation).
# Input : arr = [0, 1, 0, 3, 12]
# Output: arr = [1, 3, 12, 0, 0]

def move_zeros_to_end(arr):
    non_zero_index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1
    for i in range(non_zero_index, len(arr)):
        arr[i] = 0

# Example usage:

arr = [1, 2, 0, 4, 3, 0, 5, 0]
move_zeros_to_end(arr)
print(arr)