# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base Case 1: If the root is None, return None.
        # Base Case 2: If the root is one of the target nodes, it's the LCA.
        if not root or root == p or root == q:
            return root
        
        # Recurse on the left subtree to find p or q.
        left_result = self.lowestCommonAncestor(root.left, p, q)
        
        # Recurse on the right subtree to find p or q.
        right_result = self.lowestCommonAncestor(root.right, p, q)
        
        # If we found one node in each subtree, the current root is the LCA.
        if left_result and right_result:
            return root
        
        # If both nodes are in the left subtree, the LCA is in the left_result.
        # If both nodes are in the right subtree, the LCA is in the right_result.
        # If only one node was found, that node is its own ancestor.
        return left_result or right_result