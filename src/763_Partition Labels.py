from collections import defaultdict
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d=defaultdict(int)
        for c in s:
            d[c] += 1
        print(d)
        temp = {}
        left, right = 0,0
        count = 0
        arr=[]
        while right < len(s):
            curr = s[right]
            if curr in temp:
                temp[curr] -= 1
            else:
                temp[curr] = d[curr] -1
            if temp[curr] == 0:
                del temp[curr]
            print(temp)

            count += 1
            if not temp:
                arr.append(count)
                count = 0
            
            right += 1
        return arr
        
        
s="eccbbbbdec"
sol=Solution()
sol.partitionLabels(s)