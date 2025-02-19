nums = [2, 4, 6, 3, 5, 7, 9, 1, 8]

def minimum_index(nums):
    # set the index to zero
    min_index = -1
    # ensure any value in the list is smaller than infinity
    min_value = float('inf')
    for i in range(len(nums)):
        # here we are comparing if the num at index i in the list is greater
        # than the next iterated number
        if min_value > nums[i]:
            # if the minimum number is greater than the compared numbers (min_number)
            # and the number at index i, we skip over it can't be the number we're looking for
            min_value = nums[i] # this stores the minimum number we've seen so far
            min_index = i # we return the index of the minimum number
    return min_index

print(minimum_index(nums))

# Time complexity: O(n) - We would have to do n comparisons in the worst case
# if the element we want to find is present on the last index of the array.