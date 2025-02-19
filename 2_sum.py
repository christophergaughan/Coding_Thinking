# The number we want to search for in the list
number_to_search = 7

# List of numbers in which we want to search for the target number
nums = [2, 4, 6, 3, 5, 7, 9, 1, 8]  # Example list


# Function to find the index of the target number in the given list
def find_index(nums, target):
    """
    This function takes a list `nums` and a `target` value.
    It iterates through the list to find the first occurrence of `target`.
    If found, it returns the index; otherwise, it returns -1.

    Edge cases handled:
    1. If `nums` is empty, return -1 immediately.
    2. If `target` is None, return -1.
    3. If `target` is not in `nums`, return -1.
    4. If `nums` contains multiple instances of `target`, return the first index.
    5. Assumes `nums` contains valid, comparable values (no type mismatches).
    """

    # Corner case: Empty list
    if not nums:
        return -1  # No elements to search

    # Corner case: Target is None (invalid search)
    if target is None:
        return -1  # Prevents unnecessary iteration

    for i, val in enumerate(nums):  # Loop through each index-value pair
        if val == target:  # Check if the current value matches the target number
            return i  # Return index immediately when found

    return -1  # Target not found in the list


# Call the function with the given list and target number
index = find_index(nums, number_to_search)

# Print the result: If found, prints the index; if not found, prints -1
print(index)
