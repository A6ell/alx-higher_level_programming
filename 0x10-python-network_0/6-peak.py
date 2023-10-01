#!/usr/bin/python3
""" Find a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """
    Return a peak in a list of unsorted integers
    """
    unsorted = list_of_integers
    length = len(list_of_integers)
    if length == 0:
        return None
    elif length == 1:
        return list_of_integers[0]
    elif length == 2:
        return max(list_of_integers)

    start, end = 0, length - 1
    while start < end:
        mid = start + (end - start) // 2
        if unsorted[mid] > unsorted[mid - 1] and \
                unsorted[mid] > unsorted[mid + 1]:
            return unsorted[mid]
        if unsorted[mid - 1] > unsorted[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return unsorted[start]
