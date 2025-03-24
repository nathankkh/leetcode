from collections import defaultdict
from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        diff = [0 for _ in range(days + 2)]
        for meeting in meetings:
            diff[meeting[0]] -=1
            diff[meeting[1] + 1]+=1
        prev = days
        curr = days
        #print(diff)
        
        for i in range(1,days+2):
            diff[i] +=diff[i-1]
            
            # diff[i] = temp
            if diff[i] < 0:
                curr = prev - 1
            prev = curr

        #print(diff)
        return curr

    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        diff = defaultdict(int)
        previous_end = days
        for m in meetings:
            diff[m[0]] += 1
            diff[m[1] + 1] -= 1
            previous_end = min(m[0], previous_end)
        
        # start out with the number of days before the first meeting
        curr = previous_end - 1
        prefix = 0
        sorted_d = sorted(diff.keys())
        for start_day in sorted_d:
            if prefix == 0:
                curr = start_day - previous_end
            prefix += diff[start_day]
            previous_end = start_day

        curr += days - previous_end + 1
        return curr
    
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free = 0
        latest = 0
        for start, end in meetings:
            if start > latest + 1:
                free += start - (latest + 1)
            latest = max(latest, end)
        free += days - latest
        return free


        
        
days=5
meetings=[[2,4],[1,3]]
sol = Solution()
sol.countDays(days, meetings)


days = 8
meetings=[[3,4],[4,8],[2,5],[3,8]]
sol = Solution()
sol.countDays(days, meetings)