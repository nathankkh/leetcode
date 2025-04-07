class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def rec(index, curr_arr):
            if index == len(nums):
                res.append(curr_arr.copy())
                return
            else:
                # exclude current elem
                rec(index+1, curr_arr)
                
                # include current
                curr_arr.append(nums[index])
                rec(index+1, curr_arr)

                # Cleanup
                curr_arr.pop()
        rec(0,[])
        return res