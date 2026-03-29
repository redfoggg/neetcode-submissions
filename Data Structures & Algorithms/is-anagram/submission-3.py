from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if len(t) != len(s):
        #    return False

        #return Counter(s) == Counter(t)
        if len(t) != len(s):
            return False
        freq_s = {}
        freq_t = {}

        for i in range(len(s)):
            freq_s[s[i]] = 1 + freq_s.get(i, 0)
            freq_t[t[i]] = 1 + freq_t.get(i, 0)

        return freq_s == freq_t


    def anotherIsAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        freq_s = {}
        freq_t = {}

        for i in range(len(s)):
            freq_s[i] += 1 + freq_s.get(i, 0)
            freq_t[i] += 1 + freq_t.get(i, 0)

        return freq_s == freq_t
        