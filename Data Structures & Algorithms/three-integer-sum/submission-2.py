class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = len(nums) - 1
        nums.sort()
        res = []
        for i in range(len(nums)):
            a = nums[i]
            l = i + 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[i], nums[r]])
                    r -= 1
                    l += 1
                    while nums[i] == nums[l]:
                        l += 1
        
        return res



        