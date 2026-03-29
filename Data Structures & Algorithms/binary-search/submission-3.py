class Solution:
    def search(self, nums: List[int], target: int) -> int:
        len_ = len(nums)
        
        if len_ == 1 and target == nums[0]:
            return 0

        l, r = 0, len_ - 1
        m = (r - l)//2
        
        while l < r - 1:
            if target > nums[m]:
                l = m
                m = (r+l)//2
                continue
            elif target < nums[m]:
                r = m
                m = (r-l)//2
                continue
            else:
                return m
        return -1

            


        