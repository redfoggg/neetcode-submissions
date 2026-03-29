class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
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

            


        