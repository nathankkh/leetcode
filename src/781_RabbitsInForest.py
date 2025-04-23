class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d={}
        for a in answers:
            if a in d:
                d[a] += 1
            else:
                d[a] = 1
        count = 0 
        for k,v in d.items():
            if v < k:
                count += k+1

            else:
                count += math.ceil(v/(k+1)) * (k+1)
        return count