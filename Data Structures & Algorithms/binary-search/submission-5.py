class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        m = (r - l)//2
        if len(nums) == 1 and target == nums[0]:
            return 0
        
        while l < m:
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m
                m = (r+l)//2
                continue
            else:
                r = m
                m = (r-l)//2
                continue
        return -1

            


        