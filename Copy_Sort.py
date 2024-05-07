import os


def copy_sort(array):
    # creates a copy of the original array called 'copy'
    copy = array[:]
    # creates a new, blank array 'sorted_copy' to have elements added in
    sorted_copy = []

    # while there are elements in the array 'copy'
    while len(copy) > 0:
        minimum = 0
        for item in range(0, len(copy)):  # repeat loop until it reaches the end of the array
            # 1st loop irrelevant as 1st item is not < 1st item. 2nd loop has 2nd item < mimimum, so becomes new minimum. 3rd loop has 3rd item < than mimimum, so becomes the new minimum. 4th loop - 4th item is not < than minimum, 5th loop item is also not < minimum, 6th loop is also not < than minimum. Minimum number in this array has been found.
            if copy[item] < copy[minimum]:
                minimum = item
        # prints the item to be removed (minimum number in the current array) and the full current array.
        print('\tRemoving', copy[minimum], 'from', copy)
        # removes the minimum number from the current array and adds it into the sorted_copy array.
        sorted_copy.append(copy.pop(minimum))
    # while loop repeats, selecting the minimum number left in the 'copy' array and adding it to the end of the 'sorted_array' until 'copy' is empty.
    return sorted_copy


# Create a blank array
array = []
new_input = 0

# Displays on the screen title and original array
os.system('cls')
print('Copy Sort...')

while new_input != 'X':  # User inputs random number which, if not X, will be added into the array
    new_input = input(
        '\nEnter a random number less than 10 (X when done): ').upper()
    if new_input != 'X':
        array.append(new_input)

    print(array)

print('\n Array :', array)

# Runs the function 'copy_sort' using original array
print('\nIn ascending order :', copy_sort(array))
print('\nOriginal Array :', array)
