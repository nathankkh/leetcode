class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = {}
        for c in ransomNote:
            if c in r:
                r[c] += 1
            else:
                r[c] = 1
        for i in magazine:
            if i in r:
                r[i] -= 1
                if r[i] == 0:
                    del r[i]
        return r == {}
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}
        for c in magazine:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1
        for c in ransomNote:
            if c not in m:
                return False
            m[c] -= 1
            if m[c] == 0:
                del m[c]
        return True