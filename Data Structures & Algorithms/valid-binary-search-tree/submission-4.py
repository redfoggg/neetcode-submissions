# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left_val = root.left.val if root.left is not None else float("-inf")
        right_val = root.right.val if root.right is not None else float("inf")
        
        if root.val <= left_val or root.val >= right_val:
            return False
        
        if root.val > left_val and root.val < right_val:
            return self.isValidBST(root.left) or self.isValidBST(root.right)
        
        return True
        