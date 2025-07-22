from typing import List

class Solution:

    # extremely inefficient
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        n: number of vertices, numbered 0 -> n-1
        edges: 2d array where each elem [a,b] means there's an edge between node a and b
        
        note that if a graph is strongly connected, each node will have an edge list of every other node in the graph

        construct an adj list for the graph; for each component, check that each node has the same set of edges
        '''

        adjList = [set([i]) for i in range(n)]
        parents = [x for x in range(n)]
        ranks = [0 for _ in range(n)]

        def _find(node):
            if parents[node] == node:
                return node
            else:
                parents[node] = _find(parents[node])
                return parents[node]
        
        def _union(a,b):
            ap = _find(a)
            bp = _find(b)
            if ap == bp:
                return ap
            
            # add shorter rank to taller
            if ranks[ap] < ranks[bp]:
                parents[ap] = bp
                return bp
            elif ranks[bp] < ranks[ap]:
                parents[bp] = ap
            else:
                parents[bp] = ap
                ranks[ap] += 1
            return ap
        
        #roots = set()
        # O(E)
        for edge in edges:
            adjList[edge[0]].add(edge[1])
            adjList[edge[1]].add(edge[0])
            root = _union(edge[0], edge[1])
            #roots.add(root)

        # temp = set()
        # for comp in roots:
        #     temp.add(_find(comp))
        temp = set()
        for p in parents:
            temp.add(_find(p))
        
        res = 0
        for parent in temp:
            children = adjList[parent] 
            #expected = len(children)
            add = True
            for c in children:
                if c == parent:
                    continue
                if adjList[c] != children:
                    add = False
                    break
            if add:
                res += 1
        return res
    
n=6
edges=[[0,1],[0,2],[1,2],[3,4]]

sol = Solution()
sol.countCompleteComponents(n, edges)