# Given an array of integers and a target, return indices of two elements whose sum equals the target.
# Each input has exactly one solution, and you cannot use the same element twice.

def two_sum(nums, target):
    index_map = {}  # To store number -> index
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in index_map:
            return [index_map[complement], i]
        index_map[nums[i]] = i
    return []  # Not expected to happen as per constraints

# Example usage
print(two_sum([2, 7, 11, 15], 9))   # Output: [0, 1]
print(two_sum([3, 2, 4], 6))        # Output: [1, 2]
print(two_sum([3, 3], 6))           # Output: [0, 1]
