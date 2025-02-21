from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        '''
        len(nums) -> length of each element
        Find a binary string that does not exist in nums, of length n
        A binary number padded with 0s is also valid (e.g. 001 or 000)
        Any valid string can be returned
        '''

        # push nums into a hashset/hashtable
        d = {}
        res = ''
        n = len(nums)
        for i in nums:
            d[i] = 1

        count = 0
        while True:
            curr = bin(count)[2:]
            curr_length = len(curr)
            if curr_length != n:
                curr = '0' * (n-curr_length) + curr
            
            if d.get(curr, -1) == -1:
                return curr
            count += 1
        return
    
    
    # optimise using cantor's diagonal
    # this works because len(nums) == len(nums[i])
    # i.e. length of array == length of string in array
    # this means that the input resembles a grid
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = ''
        for i in range(len(nums)):
            if nums[i][i] == '1':
                res += '0'
            else:
                res += '1'
        return res

    
'''
[
    [0, 1, 1]
    [1, 0, 1]
    [0, 0, 0]
]

Construct result
at each step, flip the value of nums[i][i]

intuition: 
- need to find any value that does not exist in nums
- at each step, flipping a bit ensures that res != elem at current step


1:
res = 1
2:
res = 1 1
3:
res = 1 1 1

'''

    