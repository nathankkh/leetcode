from typing import List
from heapq import nlargest

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        '''
        All elems in nums are positive
        i != j
        sum of digits in nums[i] == nums[j]
        return the largest value
        '''

        def countDigits(num):
            res = 0
            for i in str(num):
                res += int(i)

            return res

        ds = {} # {sum_digits : [val, val]}
        for num in nums:
            key = countDigits(num)
            if key not in ds:
                ds[key] = [num]
            else:
                ds[key].append(num)
        # Get the largest value from the dict
        res = -1
        for lst in ds.values():
            if len(lst) < 2:
                continue
            res = max(res, sum(nlargest(2, lst)))
        return res
