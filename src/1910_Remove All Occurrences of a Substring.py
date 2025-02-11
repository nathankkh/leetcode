class Solution:
    # O ((n^2)/m)
    def removeOccurrences(self, s: str, part: str) -> str:
        # Given `s` and `part`, remove the substring `part` repeatedly until there are no more instances of it
        # return the reaminder string
        if len(part) > len(s):
            return s
        while part in s:
            #########################################
            # can rely on python's replace function #
            # which would be optimised better than  #
            # a manual implementation               #
            #########################################
            start = s.find(part)
            end = start + len(part)
            temp = s[:start] + s[end:]
            s = temp
        return s

## Faster implementations:
# - Use a stack / lazy removal?
# - KMP
##