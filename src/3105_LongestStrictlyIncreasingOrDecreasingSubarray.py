class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 0
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        longest_inc = 1
        longest_dec = 1
        
        for i in range(1,len(nums)):
            prev = nums[i - 1]
            curr = nums[i]

            if curr > prev: 
                longest_inc += 1
                if longest_dec > 1:
                    res = max(longest_dec, res)
                    longest_dec = 1
            elif curr < prev:
                longest_dec += 1
                if longest_inc > 1:
                    res = max(longest_inc, res)
                    longest_inc = 1
            else:
                res = max(res, longest_inc, longest_dec)
                longest_inc, longest_dec = 1,1
        
        return max(res, longest_inc, longest_dec)