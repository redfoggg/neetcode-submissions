class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        result = []

        for n in nums:
            freq_map[n] += 1

        for i in range(k):
            max_key = max(freq_map, key=freq_map.get)
            result.append(max_key)
            del freq_map[max_key]

        return result



        