import Lab3


def test_bubble_sort_ascending():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == expected


def test_bubble_sort_descending():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    expected = [90, 64, 34, 25, 22, 12, 11]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    assert result == expected


# REQ-03
def test_more_than_10_numbers():
    result = Lab3.bubble_sort([1,2,3,4,5,6,7,8,9,10], Lab3.SORT_ASCENDING)
    assert result == 1


# REQ-04
def test_zero_numbers():
    result = Lab3.bubble_sort([], Lab3.SORT_ASCENDING)
    assert result == 0


# REQ-05
def test_invalid_input():
    result = Lab3.bubble_sort([1, 2, "a", 4], Lab3.SORT_ASCENDING)
    assert result == 2