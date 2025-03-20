from typing import List

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # find the longest path

        u = UFDS(n)
        res = []
        
        for edge in edges:
            # [u, v, w]
            u.union(edge[0], edge[1])

        costs = [-1]*n
        # each connected component will have the same cost
        for edge in edges:
            parent = u.find(edge[0])
            costs[parent] &= edge[2]
        
        for q in query:
            p1 = u.find(q[0])
            p2 = u.find(q[1])
            if p1 != p2:
                res.append(-1)
            else:
                res.append(costs[p1])
        return res




# General idea of a UFDS
# Quickly find what set an element is in
# Can be used for an MST 
class UFDS:
    def __init__(self, n):
        '''
        Accepts an element n representing the number of elements in this UFDS
        Initialises a UFDS where all elements are disjoint
        '''
        self.ranks = [0 for _ in range(n)]
        self.parents = [x for x in range(n)]
        self.sizes = [1 for _ in range(n)]
        self.numdisjoint = n

    def find(self, element):
        if self.parents[element] == element:
            return element
        else:
            children = []
            temp = element
            # keep drilling up til parent is found
            while temp != self.parents[temp]:
                children.append(temp)
                temp = self.parents[temp]
            # path compression 
            for c in children:
                self.parents[c] = temp
        # More succinct version
        # else:
        #     self.parents[element] = self.find(self.parents[element])
        return temp


    def union(self, x, y):
        # whilst finding x and y's parent, this will do path compression
        x_parent = self.find(x)
        y_parent = self.find(y)

        # case 1: already in the same set
        if x_parent == y_parent:
            return 
        
        # case 2-n: diff set. Add the shorter one to the taller one
        # this means that the rank of the taller one should not increase, since the shorter tree is added to the root of the taller tree

        # x is shorter than y. Append X to Y. Y's size increases by X
        if self.ranks[x_parent] < self.ranks[y_parent]:
            self.parents[x_parent] = y_parent
            self.sizes[y_parent] += self.sizes[x_parent]

        # Y is shorter than X. Append Y to X. X's size increases by Y
        elif self.ranks[y_parent] < self.ranks[x_parent]:
            self.parents[y_parent] = x_parent
            self.sizes[x_parent] += self.sizes[y_parent]

        # both are equal(ish) rank. Append Y to X. 
        # X's size increases by Y. 
        # X's rank increase by 1
        else: 
            self.parents[y_parent] = x_parent
            self.sizes[x_parent] += self.sizes[y_parent]
            self.ranks[x_parent] += 1

        self.numdisjoint -= 1
    

