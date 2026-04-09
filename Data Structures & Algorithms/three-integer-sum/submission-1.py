class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l, r = 0, len(nums) - 1
        nums.sort()
        res = []
        for i in range(1, len(nums)):
            while l < r:
                if i == r or nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif i == l or nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r:
                        if nums[l] + nums[r] + nums[i] == 0:
                            l += 1
                        else:
                            break
                    while r > l:
                        if nums[l] + nums[r] + nums[i] == 0:
                            r -= 1
                        else:
                            break
                    break
        
        return res



        