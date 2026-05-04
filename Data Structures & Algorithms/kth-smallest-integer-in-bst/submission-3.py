# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def dfs(node):
            if node is None:
                return
            
            dfs(node.left) # colocando isso na frente, vamos primeiro até o leftmost value.

            arr.append(node.val) # fazemos o que precisamos sabendo que estará em ordem ascendente
            
            dfs(node.right) # aplicamos no lado direito também
        
        dfs(root)

        return arr[k-1]

        
        

