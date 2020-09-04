#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    #return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found

def linear_search_recursive(array, item, index=0):
    if index == len(array):
        return None
    if array[index] == item: # found the item, stop recursing
        return index
    else:
        result = linear_search_recursive(array, item, index+1) #increamenting by 1 every search
        return result


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    #find the middle
    #[1,5,6,7,10]
    # do a comparison of the target item to the middle item in the array
    #if the middle item is the item we are looking for, we are done and return location or index of the item
    # if the item doesnt equal to what we looking for, see if the item is less than the middle item look in the left part of the array
    # if the item is greater look in the right part of the array
    #find the middle again and repeat steps above
    left = 0
    right = len(array) - 1 #array start indexing from 0

    while left <= right:
        #find the middle index by dividing the array by half
      middle_index = (left + right) // 2
        #if the target item found, return the index
      if item == array[middle_index]:
        return middle_index
        #if the target item is less than right side, look through right side of array
      elif item < array[middle_index]:
        right = middle_index - 1
        #if the tatget item is greater than left side, look through righ left of array
      elif item > array[middle_index]:
        left = middle_index + 1


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here

    middle_index = (left + right) // 2

    if item == array[middle_inidex]: # base case
        return middle_index

    if left <= right: #2nd base case
        return None

    #recursive cases
    elif item < array[middle_inidex]:
        #move my pointers
        binary_search_iterative(array, item, left, right -1)
        

    elif item > array[middle_index]:
        #move my pointers
        binary_search_recursive(array, item, left -1, right)

if __name__ == '__main__':
    array = [1,3,5,7,9,11]
    #print(linear_search(array, 3))
    print(binary_search(array, 9))

 
