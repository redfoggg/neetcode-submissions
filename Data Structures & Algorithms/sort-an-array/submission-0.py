class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        m = len(nums) // 2
        l = nums[:m]
        r = nums[m:]

        sortedL = self.sortArray(l)
        sortedR = self.sortArray(r)

        return self.merge(sortedL, sortedR)

    
    def merge(self, l, r):
        result = []
        i = j = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                result.append(l[i])
                i += 1
            else:
                result.append(r[j])
                j += 1

        result.extend(l[i:])
        result.extend(r[j:])
        
        return result
