class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_tree_inorder(self):
        """Prints the tree in inorder traversal."""
        if self:
            if self.left:
                self.left.print_tree_inorder()
            print(self.val, end=" ")
            if self.right:
                self.right.print_tree_inorder()

    def __str__(self):
        print('left: ', self.left)
        print('val: ', self.val)
        print('right: ', self.right)

def populate_tree_from_array(arr):
    """
    Populates a binary tree from an array.

    Args:
        arr: A list representing the tree in level-order, with None for missing nodes.

    Returns:
        The root TreeNode of the constructed tree, or None if the array is empty.
    """
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = [root]
    i = 1

    while queue and i < len(arr):
        current_node = queue.pop(0)

        # Left child
        if i < len(arr) and arr[i] is not None:
            current_node.left = TreeNode(arr[i])
            queue.append(current_node.left)
        i += 1

        # Right child
        if i < len(arr) and arr[i] is not None:
            current_node.right = TreeNode(arr[i])
            queue.append(current_node.right)
        i += 1

    return root

# Example usage:
sample = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]
root = populate_tree_from_array(sample)

# Optional: Function to visualize the tree (for testing)
def print_tree_inorder(root):
    if root:
        print_tree_inorder(root.left)
        print(root.val, end=" ")
        print_tree_inorder(root.right)

# Test the population and print the result
print_tree_inorder(root)