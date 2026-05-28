
# {0: [1, 2]
#  1: []
#  2: [1]}

# {0: [1]
#  1: [0]}
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}

        for a, b in prerequisites:
            adjList[a].append(b)

        visited = set()
        def dfs(curr):
            if curr in visited:
                return False
            
            visited.add(curr)
            
            if not adjList[curr]:
                return True

            for pre in adjList[curr]:
                if not dfs(pre):
                    return False

            adjList[curr] = []
            visited.remove(curr)
            
            return True
        
        return dfs(0)
        

        


        

        

        

        
                
                

        