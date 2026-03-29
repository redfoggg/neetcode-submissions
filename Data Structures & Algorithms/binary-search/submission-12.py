class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        m = len(nums)//2

        if len(nums) == 1 and target == nums[0]:
            return 0
        
        while l <= r:
            if target == nums[m]:
                return m
            
            if target == nums[l]:
                return l
            
            if target == nums[r]:
                return r
            
            elif target > nums[m]:
                l = m
                m = (r+l)//2
                continue
            else:
                r = m
                m = (r-l)//2
                continue
        return -1

            


        