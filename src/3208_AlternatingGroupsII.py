from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:k-1])

        left, right = 0,1
        length = len(colors)
        res = 0
        while right < length:
            # option 1: not alternating
            if colors[right] == colors[right - 1]:
                left = right
                right += 1
            
            # option 2: alternating, right-left < k,  expand row
            elif right - left < k:
                right += 1
            # option 3: alternating, right - left = k, slide forward
            else:
                res += 1
                left += 1
                right += 1
        return res