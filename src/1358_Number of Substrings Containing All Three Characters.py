class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        '''
        Return number of substrings containing at least one occurence of all chars, [a,b,c]
        Count dupes as well
        '''
        left = 0
        d = {}
        res = 0

        for right in range(len(s)):
            curr = s[right]
            d[curr] = d.get(curr, 0) + 1
            
            # while the window is valid, add all substrings that 
            # end after right.
            # Since right represents the first occurrence of the third character
            # everything from right onwards is valid
            while len(d) == 3:
                res += (len(s) - right)
                old = s[left]
                d[old] -= 1
                if d[old] == 0:
                    del d[old]
                left += 1
            
        return res
    
sol = Solution()
sol.numberOfSubstrings('aaacb')