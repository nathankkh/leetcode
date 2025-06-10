class Solution:
    def maxDifference(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return max([x for x in d.values() if x%2 == 1]) - min([x for x in d.values() if x%2==0])