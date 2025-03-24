from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        s, e = 0, 0
        res = []
        curr = [intervals[0][0],intervals[0][1]]
        for start, end in intervals:
            if curr[1] >= start:
                curr[1] = max(end, curr[1])
            else:
                res.append(curr)
                curr = [start, end]
        res.append(curr)
        return res
