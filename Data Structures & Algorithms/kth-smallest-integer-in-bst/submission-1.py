# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def dfs(node, k):
            if node is None:
                return
            
            dfs(node.left, k)

            arr.append(node.val)
            
            dfs(node.right, k)
        
        dfs(root, k)

        return arr[k-1]

        
        

