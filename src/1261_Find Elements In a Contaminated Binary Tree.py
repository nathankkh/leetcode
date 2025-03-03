from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        # initialise the tree
        # recover the tree -> contaminated tree means that every node is -1
        # root will always be 0
        # node.left.val = 2 * currval + 1
        # node.right.val = 2 * currval + 2
        self.tree = root
        self.tree.val = 0
        self.hashset = set([0])

        self.recover(self.tree)


    def find(self, target: int) -> bool:
        if target in self.hashset:
            return True
        return False

    def recover(self, node) :
        if not node:
            return

        else:
            if node.left:
                node.left.val = node.val * 2 + 1
                self.hashset.add(node.val * 2 + 1)
                self.recover(node.left)
            
            if node.right:
                node.right.val = node.val  * 2 + 2
                self.hashset.add(node.val  * 2 + 2)
                self.recover(node.right)
        

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

