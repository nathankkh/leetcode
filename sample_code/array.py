from typing import List


# counting subarrays
def subarrays_from_array(arr: List) -> int:
    # get the length of the array
    n = len(arr)

    # mathematical formula:
    return (n* (n + 1)) // 2

