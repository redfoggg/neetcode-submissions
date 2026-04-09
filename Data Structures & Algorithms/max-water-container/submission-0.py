class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, max_a = 0, len(heights) - 1, 0

        while l < r:
            curr_a = min(heights[l], heights[r]) * (r - l)
            max_a = max(max_a,  curr_a)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_a



        