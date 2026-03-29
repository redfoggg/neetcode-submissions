class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_map = {}
        majority = len(nums)//2

        for i in nums:
            freq_map[i] = freq_map.get(i, 0) + 1
        
        return max(freq_map, key=freq_map.get)

                




        