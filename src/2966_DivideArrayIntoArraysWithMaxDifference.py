class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res = []
        for i in range(0,n,3):
            x,y,z = nums[i],nums[i+1],nums[i+2]
            if z-x > k:
                return [] # early termination - since len(nums) is a multiple of 3 and the answer must be of length n/3, all subarrays must be valid
            res.append([x,y,z])
        return res
            