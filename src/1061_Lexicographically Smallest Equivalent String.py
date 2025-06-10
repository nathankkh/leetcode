class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parents = [chr(x) for x in range(97, 123)]  # store as a string

        def _find(elem):  # accepts a string
            idx = ord(elem) - 97
            if parents[idx] == elem:
                return parents[idx]
            else:
                parents[idx] = _find(parents[idx])
                return parents[idx]

        def _union(x, y):
            x_p = _find(x)
            y_p = _find(y)
            if x_p == y_p:
                return
            if x_p < y_p:
                parents[ord(y_p) - 97] = x_p
            else:
                parents[ord(x_p) - 97] = y_p

        for i in range(len(s1)):
            _union(s1[i], s2[i])

        out = []
        for i in baseStr:
            out.append(_find(i))
        return ''.join(out)