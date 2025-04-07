from typing import List

class Solution:
    # option 1
    def majorityElement(self, nums: List[int]) -> int:
        curr_count = 0
        res = None

        for num in nums:
            if curr_count == 0:
                res = num
                curr_count += 1
            elif num != res:
                curr_count -= 1
            else:
                curr_count += 1
        return res
    

    # option 2
    def majorityElement(self, nums: List[int]) -> int:
        curr_count = 1
        res = nums[0]

        for i in range(1,len(nums)):
            if nums[i] == res:
                curr_count += 1
            else:
                curr_count -= 1
                if curr_count == 0:
                    curr_count = 1
                    res = nums[i]
        return res