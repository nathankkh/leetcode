from typing import List;

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        z=0
        for num in nums:
            if num ==0:
                z+=1
                continue
            if num > 0:
                break
            else:
                count += 1
        return max(count, n-count-z)
    
    def maximumCountBS(self, nums):
        n = len(nums)
        neg_count = 0
        pos_count = 0

        # Find the last negative index
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < 0:
                neg_count = mid + 1
                left = mid + 1
            else:
                right = mid - 1

        # Find the first positive index
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > 0:
                pos_count = n - mid
                right = mid - 1
            else:
                left = mid + 1

        return max(neg_count, pos_count)
nums = [5,20,66,1314]
sol = Solution()
sol.maximumCountBS(nums)