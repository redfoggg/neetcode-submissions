class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 1:
            return True
        
        visited = set()
        adj = {i:[] for i in range(numCourses)}
        for n1, n2 in prerequisites:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                
                if not dfs(j, i):
                    return False
                
            return True
        
        return dfs(0, -1)
                
                

        