class Solution:
    def clearDigits(self, s: str) -> str:
        q = []
        for i in range(len(s)):
            curr = s[i]
            if '0' <= s[i] <= '9':# isnumber
                if q:
                    q.pop()
            else:
                q.append(curr)
        
        return ''.join(q)
        
        
sol= Solution()
tc = 'abc'
out = sol.clearDigits(tc)
assert(out == 'abc')

tc='cb34'
out=sol.clearDigits(tc)
assert(out == '')

tc='c3bam34'
out=sol.clearDigits(tc)
assert(out == 'b')