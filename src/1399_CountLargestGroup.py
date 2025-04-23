from collections import defaultdict
class Solution:
    def countLargestGroup(self, n: int) -> int:
        d=defaultdict(int)
        for i in range(1,n+1):
            s = sum(int(x) for x in str(i)) # use divmod and keep dividing by 10 to avoid converting to string
            d[s] += 1

        highest = max(d.values())
        return sum(1 for x in d.values() if x == highest)