from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # (n*(n+1))/2
        res=0
        left = 0
        right = 0
        while right < len(nums):
            if nums[right]!=0:
                if left != right or right == len(nums)-1:
                    
                    length = right - left 
                    res += (length*(length+1))//2
                    # close sliding window
                right += 1
                left = right
            else:
                right += 1

        return res

tc = [
    ([1,3,0,0,2,0,0,4],6),
    ([0,0,0,2,0,0],9),
    ([2,10,2019],0)
]

sol = Solution()
for test,ans in tc:
    print(sol.zeroFilledSubarray(test) == ans)