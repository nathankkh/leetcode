# https://leetcode.com/problems/3sum/
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort() # n logn
        res = set()
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i > 0:
                continue
            if nums[i] > 0:
                break

            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1
        
        out = []
        for i in res:
            out.append(list(i))
        return out
'''
i + j + k = 0

i = -(j + k)

dict 1
i: remainder

dict 2
i: {[j1, k2], [j2, k2]}
'''

'''
array[i], array[j], array[k] such that they add up to 0

Return a list of lists, of each combination of the values of arr[i/j/k]. Order does not matter
'''