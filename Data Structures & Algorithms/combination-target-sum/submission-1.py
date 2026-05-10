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