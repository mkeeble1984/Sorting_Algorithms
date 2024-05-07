def copy_sort(array):
    # creates a copy of the original array called 'copy'
    copy = array[:]
    # creates a new, blank array 'sorted_copy' to have elements added in
    sorted_copy = []

    # while there are elements in the array 'copy'
    while len(copy) > 0:
        minimum = 0
        for element in range(0, len(copy)):
            if copy[element] < copy[minimum]:  # NEED TO UNDERSTAND WHAT IS HAPPENEING HERE
                minimum = element
        print('\tRemoving', copy[minimum], 'from', copy)
        sorted_copy.append(copy.pop(minimum))

    return sorted_copy


# Adds data into the array
array = [5, 3, 1, 2, 6, 4]

# Displays on the screen Title and original array
print('Copy Sort...')
print('Array :', array)

# Runs the function 'copy_sort' using original array
print('Copy :', copy_sort(array))
print('Array :', array)

# Test to see if it worked
