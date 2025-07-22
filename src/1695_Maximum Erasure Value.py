from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        curr = 0
        res = 0
        d=set()
        for right in range (len(nums)):
            if nums[right] not in d:
                d.add(nums[right])
                curr += nums[right]
                res = max(curr, res)
            else:
                while True:
                    if nums[left] == nums[right]:
                        left += 1
                        break
                    else:
                        d.discard(nums[left])
                        curr -= nums[left]
                        left += 1
        return res