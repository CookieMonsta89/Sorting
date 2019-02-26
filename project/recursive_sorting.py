### helper function
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range( 0, elements ):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


### recursive sorting function
def merge_sort( arr ):
    if len( arr ) > 1:
        left = merge_sort( arr[ 0 : len( arr ) / 2 ] )
        right = merge_sort( arr[ len( arr ) / 2 : ] )
        arr = merge( left, right )   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION
def quick_sort( arr, low, high ):
    if high - low <= 0:
        return arr
        # base case above, returns array in last position minus zeroeth is less than 0
        # first rule which is to have a base case
    startingPoint = low
    # second rule which is have a path to the base case
    for i in range(startingPoint+1, high+1):
        # iterated less than zeroeth spot which now is 0 spot
        if arr[i] < arr[startingPoint]: 
            # setting variable to the iterated position
            mark = arr[i]
            # setting iterated position to next position
            arr[i] = arr[startingPoint + 1]
            # setting iterated position to mark which is value of iterated position of array
            arr[startingPoint + 1] = mark
            # mark being set to arrow low which is zeroeth 
            mark = arr[startingPoint]
            # zeroeth being set to next position 
            arr[startingPoint] = arr[startingPoint + 1]
            # setting next position equal to mark which is the arr[low]
            arr[startingPoint + 1] = mark
            # incrementing starting point and setting it equal to one.
            startingPoint += 1
    # this is the third rule here which is calling the function 
    arr = quick_sort(arr, low, startingPoint - 1)
    arr = quick_sort(arr, startingPoint + 1, high)

    return arr

sortme = [2,1,4,5,3,6]

print(quick_sort(sortme, 0, len(sortme)-1 ))


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
