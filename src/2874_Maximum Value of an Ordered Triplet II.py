from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]*n
        suffix = [0]*n
        prefix[0] = nums[0] # stores the maximum value of i thus far
        suffix[-1] = nums[-1] # stores the maximum value of k thus far (when iterating through j, what is the max value of k to the right?)
        for i in range(1,n):
            prefix[i] = max(prefix[i-1], nums[i])
        for i in range(n-2, -1, -1):
            suffix[i] = max(suffix[i+1], nums[i])
        res = 0
        for j in range(1, n-1):

            res = max(res, (prefix[j-1] - nums[j]) * suffix[j+1])
        return res
    
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res, max_i, max_diff = 0,0,0
        for k in nums:
            res = max(res, max_diff * k)
            max_diff = max(max_diff, max_i - k) #  if j (for the next loop) is curr
            max_i = max(max_i, k) #  if i (for the next loop) is curr. update max i val with curr, since curr has already been checked

        return res
    
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        highestSeen = 0
        highestDiff = 0
        ans = 0
        for num in nums:
            if highestDiff*num > ans:
                ans = highestDiff*num
            if highestSeen-num > highestDiff:
                highestDiff = highestSeen-num
            if num > highestSeen:
                highestSeen = num
        return ans

tc=  [12,6,1,2,7]
sol = Solution()
sol.maximumTripletValue(tc)