class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq, nums_set = 0, set(nums)

        for num in nums:
            if (num - 1) not in nums_set:
                count = 0
                while (num + count) in nums_set:
                    count += 1
                max_seq = max(count, max_seq)
        
        return max_seq


                



        