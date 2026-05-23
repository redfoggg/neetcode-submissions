class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            sum_ = numbers[l] + numbers[r]
            if sum_ == target:
                return [numbers[l], numbers[r]]
            elif sum_ < target:
                l += 1
            else:
                r -= 1
            
        
        return [numbers[l], numbers[r]]
        