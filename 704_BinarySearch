class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right :
            # print(list[left])
            # print(list[mid])
            # print(list[right])
            # print()
            mid = ((right + left) // 2)
            curr = nums[mid]
            if target == curr: 
                return mid
            
            if target > curr:
                left = mid + 1
            else:
                right = mid - 1
            

        return -1