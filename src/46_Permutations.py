class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr = []
        if len(nums) == 1:
            return [nums]
        n = len(nums)
        used = [False] * n
        def helper(curr):
            
            if len(curr) == n:
                arr.append(curr.copy())
                return
            else:
                for i in range(n):
                    if used[i]: 
                        continue
                    else:
                        used[i] = True
                        curr.append(nums[i])
                        helper(curr)
                        used[i] = False
                        curr.pop()
        
        helper([])
        return arr