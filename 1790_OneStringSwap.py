class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swap = []
        # idx: [c1, c2]
        if s1 == s2:
            return True
        
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            else:
                swap.append( [s1[i], s2[i]] )
                if len(swap) > 2:
                    return False
        if len(swap) == 1:
            return False
        else:
        # check if idx1[c1] == idx2[c2] and vice versa
            return swap[0][0] == swap[1][1] and swap[0][1] == swap[1][0]
        
        