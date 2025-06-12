# Given an array where each element is a vote, return all candidates with votes > n/3.
# If none, return an empty list. Return result in sorted order.

def majority_element_n_by_3(arr):
    from collections import Counter

    n = len(arr)
    threshold = n // 3
    count = Counter(arr)
    # Filter elements with count > n/3 and return sorted result
    return sorted([num for num, freq in count.items() if freq > threshold])


# Example usage
print(majority_element_n_by_3([2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]))  # Output: [5, 6]
print(majority_element_n_by_3([1, 2, 3, 4, 5]))                   # Output: []
