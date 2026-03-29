from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        visited = set()

        for i in range(len(strs)):
            if strs[i] in visited:
                continue
            grouped = [strs[i]]
            visited.add(strs[i])
            for j in range(i+1, len(strs)):
                if self.isAnagram(strs[i], strs[j]):
                    visited.add(strs[j])
                    grouped.append(strs[j])
            
            result.append(grouped)
        
        return result

    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)

        