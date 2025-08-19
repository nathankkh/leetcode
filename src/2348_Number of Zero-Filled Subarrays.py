from typing import List
# 1, 3, 6, 10, 15
# 1 + 2 + 3 + 4 + 5
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # (n*(n+1))/2
        res=0
        curr=0
        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1
                res += curr
            else:
                curr = 0
        return res

tc = [
    ([1,3,0,0,2,0,0,4],6),
    ([0,0,0,2,0,0],9),
    ([2,10,2019],0)
]

sol = Solution()
for test,ans in tc:
    print(sol.zeroFilledSubarray(test) == ans)