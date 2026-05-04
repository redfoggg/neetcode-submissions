# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 1
        res = root.val
        def dfs(node, k):
            nonlocal res
            nonlocal count
            if node is None:
                return
            
            if count == k:
                res = node.val
                if node.left:
                    res = node.left.val
                count += 1
                return
            elif count > k:
                return
            
            count += 1
            dfs(node.left, k)
            dfs(node.right, k)
        
        dfs(root, k)

        return res

        
        

