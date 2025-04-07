class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n=len(nums)
        dp = [1]*n
        idx = [-1]*n
        max_idx = 0

        for i in range(n):
            curr = nums[i]
            for j in range(i):
                if curr % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j]+1 # store the size of the largest subset thus far
                    idx[i] = j # store the most recent element that is valid
                
            if dp[i] > dp[max_idx]:
                max_idx = i
        
        res = []
        while max_idx != -1:
            res.append(nums[max_idx])
            max_idx = idx[max_idx]
        return res
