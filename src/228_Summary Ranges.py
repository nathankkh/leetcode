from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        l=0
        n = len(nums)
        if n == 1:
            return [str(nums[0])]
        if n == 0:
            return []
        for r in range(1,n):
            if nums[r] - 1 == nums[r-1]:
                if r == n-1:
                    res.append(f'{nums[l]}->{nums[r]}')
                    return res
            else:
                if r - l == 1:
                    res.append(str(nums[l]))
                else:
                    res.append(f'{nums[l]}->{nums[r-1]}')
                l = r
        
        
        res.append(str(nums[-1]))

        return res
    
