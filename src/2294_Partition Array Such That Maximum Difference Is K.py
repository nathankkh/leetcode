from typing import List

# partition nums into one or more subsequences so that each element appears in only one subsequence
# difference elements in a subsequence must be <= k
# return min number of subsequences
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        if k == 0:
            return len(set(nums))
        nums.sort()
        base = nums[0]
        res = 1
        for num in nums:
            if num - base > k:
                res += 1
                base = num
        return res