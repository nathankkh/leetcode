from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head or not root:
            return False

        # Check if a path starting from this node matches the linked list
        def checkPath(listNode, treeNode):
            if not listNode:
                return True
            if not treeNode:
                return False
            if treeNode.val != listNode.val:
                return False

            return checkPath(listNode.next, treeNode.left) or checkPath(
                listNode.next, treeNode.right
            )

        # Try starting the path from the current node
        if checkPath(head, root):
            return True

        # If no match found starting from current node, try with children
        if root.left and self.isSubPath(head, root.left):
            return True
        if root.right and self.isSubPath(head, root.right):
            return True

        return False
