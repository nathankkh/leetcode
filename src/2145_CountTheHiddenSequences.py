from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prev = 0
        min_val = 0
        max_val = 0
        for i in range(1, len(differences) + 1):
            curr = prev + differences[i - 1]
            if min_val > curr:
                min_val = curr
            if max_val < curr:
                max_val = curr
            prev = curr
            if max_val - min_val > upper - lower:
                return 0

        return (upper - lower) - (max_val - min_val) + 1
