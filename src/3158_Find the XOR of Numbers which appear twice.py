from typing import List
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res=0
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                res^=nums[i]
        return res
    def duplicateNumbersXOR(self, nums:List[int]) -> int:
        res=0
        d={}
        for num in nums:
            if num in d:
                res ^= num
            else:
                d[num] = 1
        return res