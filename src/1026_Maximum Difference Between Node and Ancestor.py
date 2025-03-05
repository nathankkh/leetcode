import math
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        '''
        Find max value v, where
        v = a.val - b.val
        a is somewhere above b in the tree
        
        '''

        def dfs(node, min_v, max_v):
            if not node:
                return max_v - min_v
            
            min_v = min(node.val, min_v)
            max_v = max(node.val, max_v)

            left= dfs(node.left, min_v, max_v)
            right = dfs(node.right, min_v, max_v)
            return max(left, right)
        return dfs(root, math.inf, -1)