import bisect

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[k] != val:
                k += 1
            if nums[i] != val and i > k:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
            
        return k


        