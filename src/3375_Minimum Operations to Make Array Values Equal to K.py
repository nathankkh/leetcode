from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        '''
        1. find an int `h`, which is a number such that any value greater than `h` is identical in nums
        2. For ALL values greater than `h`, change them to `h` (this counts as one op)
        3. evntually set h to k and change all values to that
        4. return # of operations, or -1 if impossible

        This means that for every step, (second largest element <= `h` < Largest element) 
        -> greedy: 

        If k > h, definitely false. If k < all elems, definitely true

        '''

        a = set(nums)
        count = 0
        for val in a:
            if val < k:
                return -1
            elif val > k:
                count += 1
        return count
    

    def minOperations(self, nums: List[int], k: int) -> int:

        a = set()
        for num in nums:
            if num < k:
                return -1
            elif num > k:
                a.add(num)

        return len(a)