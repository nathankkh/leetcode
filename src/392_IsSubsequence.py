class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        if t == '' or len(t) < len(s):
            return False
        i,j=0,0
        n=len(s)
        o=len(t)
        while i < n:
            if j == o:
                return False
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                j+=1
        return True
