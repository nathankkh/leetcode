from typing import List
from collections import defaultdict
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        '''
        returns a list, where each element is the number of distinct colours at ith stage

        constraints:
        -> limit >= 1; at least 2 balls
        -> queries: at least 1 query
        '''
        balls = {} # ball_n: colour
        colours = {} # color_n: count
        running_count = 0
        res=[]
        for query in queries:
            # ball[i] DNE: check colours[colour]. count + 1
            # ball[i] exists -> decrement colours[current]. If colours[colour] == 0, decrement running_count. if colours[new] DNE, add to running_count
            current = 0
            if query[0] in balls:
                # get current colour
                current = balls[query[0]]
            # update new colour of balls
            balls[query[0]] = query[1]
            
            if current: # this will mean that it already exists in colours
                # check current 
                if colours[current] > 1:
                    colours[current] -= 1
                else:
                    colours.pop(current)
                    running_count -= 1
            
            # update colours dict
            if query[1] in colours:
                colours[query[1]] += 1
            else:
                colours[query[1]] = 1
                running_count += 1
            res.append(running_count)
        return res



