#Given an array of positive integers arr[], return the second largest element
#from the array. If the second largest element doesn't exist then return -1.
#Note: The second largest element should not be equal to the largest element.

def second_largest(self, arr):
    if len(arr) < 2:
        return -1

    first = second = -1

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second if second != -1 else -1


# Example usage:
arr = [12,35,1,10,34,1]
sl = second_largest(None, arr)
print(sl)