class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = {}
        for i in range(len(nums)):
            if nums[i] in visited:
                return True
            visited[nums[i]] = i

        
        return False
        