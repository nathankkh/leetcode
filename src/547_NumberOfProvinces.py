class Solution:
    #UFDS
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parents=[i for i in range(n)]
        ranks = [0 for _ in range(n)]
        disjoint = n

        def _find(node):
            if parents[node] == node:
                return node
            else:
                parents[node] = _find(parents[node])
                return parents[node]
        
        def _union(a,b, disjoint):
            ap = _find(a)
            bp = _find(b)
            if ap == bp:
                return disjoint
            # union smaller to bigger
            if ranks[ap] < ranks[bp]:
                parents[ap] = bp
            elif ranks[bp] < ranks[ap]:
                parents[bp] = ap
            else:
                parents[bp] = ap
                ranks[ap] += 1
            return disjoint - 1

        for i in range(n):
            arr = isConnected[i]
            for j in range(n):
                if i == j:
                    continue
                if arr[j] == 1:
                    disjoint = _union(i,j,disjoint)
        return disjoint
