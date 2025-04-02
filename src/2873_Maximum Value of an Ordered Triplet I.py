import math

from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # (nums[i] - nums[j]) * nums[k]
        greatest_val = 0
        greatest_diff =0
        best_res = 0

        for idx in range(len(nums)):
            best_res = max(best_res, greatest_diff * nums[idx])
            greatest_diff = max(greatest_diff, greatest_val - nums[idx]) if idx > 0 else greatest_diff
            greatest_val = max(greatest_val, nums[idx])
            

        return max(best_res,0)


# tc = [18,15,8,13,10,9,17,10,2,16,17]
#tc = [8, 6, 3, 13, 2, 12, 19, 5, 19, 6, 10, 11, 9]
tc=[2,3,1]
sol = Solution()
sol.maximumTripletValue(tc)
