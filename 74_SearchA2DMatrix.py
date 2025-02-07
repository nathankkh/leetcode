class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # edge case: empty matrix
        if not matrix:
            return False
        # edge case: check largest and smallest elements
        smallest = matrix[0][0]
        largest = matrix[-1][-1]
        if target < smallest or target > largest:
            return False
        
        row_length = len(matrix[0])
        top, bot = 0, len(matrix) - 1
        res = -1
        while top <= bot:
            mid = (top + bot) // 2
            mid_start = matrix[mid][0]
            mid_end = matrix[mid][row_length - 1]
            
            if target <= mid_end and target >= mid_start: # correct row
                res = self.bin_search_row(matrix[mid],target)
                break

            elif target < mid_start:
                bot = mid - 1
            elif target > mid_end:
                top = mid + 1
            else:
                return False
        return res != -1

        
    def bin_search_row(self, lst, target):
        l, r = 0, len(lst) - 1
        while l <= r:
            mid = (l + r) // 2
            if lst[mid] == target:
                return mid
            elif lst[mid] < target:
                l = mid + 1
            elif lst[mid] > target:
                r = mid - 1
            else:
                return -1
        return -1