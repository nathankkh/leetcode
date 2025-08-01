class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return 1
        m = max(nums)
        
        count = 1 if nums[0]==m else 0
        res = count
        for i in range(1,len(nums)):
            if nums [i] == m:
                count += 1
            else:
                count =0
            if count > res:
                res = count
                
        return res