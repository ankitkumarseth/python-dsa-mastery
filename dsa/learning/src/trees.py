from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Trees:
    """
    Practice fundamental Tree algorithms using Recursion (DFS) and Queues (BFS).
    """

    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Given the root of a binary tree, invert the tree, and return its root.
        """
        # TODO: Implement this using Recursion (DFS).
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invert_tree(root.left)
        self.invert_tree(root.right)
        return root

    def max_depth(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, return its maximum depth.
        """
        if root is None:
            return 0

        return max(self.max_depth(root.right), self.max_depth(root.left))+ 1
