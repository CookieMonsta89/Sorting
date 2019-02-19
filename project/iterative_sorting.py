# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
             



        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]



    return arr

print(selection_sort(['joe', 'matt', 'bill', 'ti', 'william', 'andy']))


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    for index in range(1, len(arr)):
        cur_value = arr[index]
        cur_index = index

        while cur_index > 0 and arr[cur_index - 1] > cur_value:
            arr[cur_index] = arr[cur_index - 1]
            cur_index = cur_index - 1

        arr[cur_index] = cur_value

    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr) - 1, 0, -1):
        for i in range(i):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

    return arr

arr = [2,3,3,6,1,23,45, 56,2]
bubble_sort(arr)
print(arr)
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if len(arr) == 0:
        return arr
    m = max(arr) + 1

    return arr
    