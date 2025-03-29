from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        """
        dominant value: if an element is a majority element
        It is guaranteed that nums contains exactly one dominant value

        A valid split: Both subarrays have the same dominant element
        (note that a subarray of length 1 -> that element is dominant)

        Return the smallest index that results in a valid split, else -1
        This will be the index of the last element of the first subarray
        """

        # determine what the dominant value is
        domElement = nums[0]
        domCount = 1
        n = len(nums)
        for i in range(1, n):
            if nums[i] == domElement:
                domCount += 1
            else:
                domCount -= 1
            if domCount == 0:
                domCount = 1
                domElement = nums[i]

        prefix = [0 for _ in range(n)]
        domCount = 0  # start tracking total number of dom element
        if nums[0] == domElement:
            prefix[0] = 1
            domCount = 1
        for i in range(1, n):
            if nums[i] == domElement:
                prefix[i] = prefix[i - 1] + 1
                domCount += 1
            else:
                prefix[i] = prefix[i - 1]

        # find the smallest split that keeps that as the dominant value

        # iterate through prefix array - if prefix val > length of subarray/2 so far AND (domCount - current prefix value) >= length of remaining subarray

        # check if split is at 0
        if prefix[0] == 1 and (domCount - 1) > (n - 1) // 2:
            return 0
        for i in range(1, n - 1):
            if prefix[i] > ((i + 1) // 2) and domCount - prefix[i] > (n - (i + 1)) // 2:
                return i

        # if we split at the last element
        if prefix[-1] == domElement and (domCount - 1) > (n - 1) // 2:
            return n - 2

        return -1
