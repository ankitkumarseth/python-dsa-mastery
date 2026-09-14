import pytest
from src.trees import Trees, TreeNode

class TestTrees:
    
    def setup_method(self):
        self.sol = Trees()

    def test_invert_tree(self):
        # [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]
        root = TreeNode(4, 
            TreeNode(2, TreeNode(1), TreeNode(3)), 
            TreeNode(7, TreeNode(6), TreeNode(9))
        )
        inv = self.sol.invert_tree(root)
        assert inv.val == 4
        assert inv.left.val == 7
        assert inv.right.val == 2
        assert inv.left.left.val == 9
        assert inv.right.right.val == 1

    def test_max_depth(self):
        # [3,9,20,null,null,15,7] -> 3
        root = TreeNode(3, 
            TreeNode(9), 
            TreeNode(20, TreeNode(15), TreeNode(7))
        )
        assert self.sol.max_depth(root) == 3

        root2 = TreeNode(1, None, TreeNode(2))
        assert self.sol.max_depth(root2) == 2
        
        assert self.sol.max_depth(None) == 0
