# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        while q: # todo resto é simplesmente como devemos fazer um BFS
            qLen = len(q)
            level = [] # questão em si
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val) # parte da questão em si
                    q.append(node.left)
                    q.append(node.right)
            if level: # questão em si
                res.append(level) # questão em si
        
        return res
        