
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
            
            if not adjList[curr]:
                return True

            visited.add(curr)
            for pre in adjList[curr]:
                if not dfs(pre):
                    return False

            adjList[curr] = []
            visited.remove(curr)
            
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True


        

        


        

        

        

        
                
                

        