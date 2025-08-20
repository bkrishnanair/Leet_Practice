# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def get_leaf_sequence(root, leaves):
            if not root:
                return

            if not root.left and not root.right:
                leaves.append(root.val)
            
            get_leaf_sequence(root.left, leaves)
            get_leaf_sequence(root.right, leaves)

        leaves1 = []
        leaves2 = []
        
        get_leaf_sequence(root1, leaves1)
        get_leaf_sequence(root2, leaves2)
        
        return leaves1 == leaves2     