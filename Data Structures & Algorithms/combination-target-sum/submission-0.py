class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        
        def backtrack(i, currList, total):
            if total == target:
                res.append(currList[:])
                return

            for j in range(i, len(nums)):
                if (total + nums[j]) > target:
                    break
                currList.append(nums[j])
                backtrack(j, currList, total + nums[j])
                currList.pop()
                
    
        backtrack(0, [], 0)
        
        return res
    

    def is_solution(self, path, target):
        if sum(path) == target:
            return True
        return False

    def is_valid(self, choice, target):
        if (target - choice) >= 0:
            return True
        return False




        