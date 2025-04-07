class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        def rec(index, current_sum):
            if index == n:
                return current_sum
            else:
                include = rec(index + 1, current_sum^nums[index])
                exclude = rec(index + 1, current_sum)
                return include + exclude

        return rec(0,0)