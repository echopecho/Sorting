# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            smallest_element = arr[i] if arr[i] < arr[j] else arr[j]
            largest_element = arr[i] if arr[i] > arr[j] else arr[j]
            arr[i] = smallest_element
            arr[j] = largest_element

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swap = True

    while swap:
        count = 0
        for i in range(0, len(arr) - 1):
            j = i + 1
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                count += 1
        swap = False if count == 0 else True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    count_arr = [0 for i in range(0, maximum + 1)]
    for i in arr:
        count_arr[i] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    final_arr = [0 for i in range(0, len(arr))]
    for i in range(0, len(arr)):
        right_index = count_arr[arr[i]] - 1
        count_arr[arr[i]] -= i
        final_arr[right_index] = arr[i]
    return final_arr


print(count_sort([3, 5, 4, 1, 2], 5))

