# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


class Solution:
    def topKFrequent(self, num, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for x in num:
            if d[x]:
                d[x] += 1
            else:
                d[x] = 1

        