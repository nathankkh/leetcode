from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def helper(root: Optional[TreeNode]):
            if root == None:
                return (0,0)

            left_skip, left_rob = helper(root.left)
            right_skip, right_rob = helper(root.right)

            # if curr robbed, skip children
            robbed = root.val + left_skip + right_skip

            # if skipped, rob children
            skipped = max(left_skip, left_rob) + max(right_skip, right_rob)

            return (skipped, robbed)
        
        return max(helper(root))