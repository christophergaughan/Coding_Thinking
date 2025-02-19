nums = [2, 4, 6, 3, 5, 7, 9, 1, 8]


def maximum_index(nums):
    # set the index to 0
    max_index = -1
    # make the max val such that any number in the list will be greater than this
    max_val = float('-inf')
    for i in range(len(nums)):
        # This will always be the case, you've insured that you can go through the list from the first index
        if max_val < nums[i]:
            # at the beginning the first number in nums is checked
            # as we loop through the list `max_val`- the number- is compared with `max_val`
            max_val = nums[i]
            max_index = i
    return max_index
print(maximum_index(nums))

# Time complexity: O(n) - We would have to do n comparisons in the worst case
# if the element we want to find is present on the last index of the array.