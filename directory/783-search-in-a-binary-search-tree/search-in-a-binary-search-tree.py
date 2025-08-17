# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #ITERATIVE:
        # Base Case: If the root is null or we found the value.
        if not root or root.val == val:
            return root
        
        # If the value is smaller, search the left subtree.
        if val < root.val:
            return self.searchBST(root.left, val)
        
        # Otherwise, search the right subtree.
        return self.searchBST(root.right, val)

'''
property that all nodes in the left subtree have values less than the root, and all nodes in the right subtree have values greater

Iterative Solution  more efficient for an interview setting as it avoids the overhead of the recursion call stack, resulting in O(1) space complexity.

RECURSIVE:
 # Base Case: If the root is null or we found the value.
        if not root or root.val == val:
            return root
        
        # If the value is smaller, search the left subtree.
        if val < root.val:
            return self.searchBST(root.left, val)
        
        # Otherwise, search the right subtree.
        return self.searchBST(root.right, val)

'''