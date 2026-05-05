print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):

    # REQ-04: 0 numbers
    if len(arr) == 0:
        return 0

    # REQ-03: >= 10 numbers
    if len(arr) >= 10:
        return 1

    # REQ-05: non-integer values
    for val in arr:
        if not isinstance(val, int):
            return 2

    # Copy input list to results list
    arr_result = arr.copy()

    # Get number of elements in the list
    n = len(arr_result)

    if n < 10:
        for i in range(n - 1):
            for j in range(0, n - i - 1):

                if sorting_order == SORT_ASCENDING:
                    if arr_result[j] > arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

                elif sorting_order == SORT_DESCENDING:
                    if arr_result[j] < arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

                else:
                    # keep your original behaviour
                    arr_result = []

    return arr_result
