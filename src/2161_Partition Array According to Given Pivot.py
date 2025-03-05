from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        '''
        less than pivot | pivot & equivalent values | greater than pivot
        relative order is maintained
        '''
        less=[]
        more=[]
        pivot_count = 0
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot: 
                pivot_count += 1
            else:
                more.append(num)
        
        less.extend([pivot]*pivot_count)
        less.extend(more)
        return less
    
sol = Solution()
nums1=[9,12,5,10,14,3,10]
pivot = 10
print(sol.pivotArray(nums1, pivot))
