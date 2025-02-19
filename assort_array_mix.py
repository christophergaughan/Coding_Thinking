def selection_sort(lst):
    """
    Selection sort function
    :param lst: List of integers
    """

    # Traverse through all lst elements
    # you're kind of setting up your first pointer here
    for i in range(len(lst)):
        # Find the minimum element in unsorted lst
        min_index = i
        # note here we are starting our pointer 1 index ahead of i
        for j in range(i + 1, len(lst)):
            # This is the part of the code that does most of the heavy lifting
            # it is asking: True or False- is the number at index i > greater than
            # the number at index j- if True- j becomes the index
            if lst[min_index] > lst[j]:
                min_index = j

        # Swap the found minimum element with the first element
        lst[i], lst[min_index] = lst[min_index], lst[i]


# Driver code to test above
if __name__ == '__main__':
    lst = [3, 2, 1, 5, 4]
    selection_sort(lst)  # Calling selection sort function

    # Printing Sorted lst
    print("Sorted lst: ", lst)
