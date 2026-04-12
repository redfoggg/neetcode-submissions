class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = res = 0
        allowed = k

        for r in range(len(s)):
            if s[r] != s[l] and allowed > 0:
                allowed -= 1
            elif s[r] != s[l] and allowed == 0:
                l = r
                allowed = k
            res = max(res, r - l + 1)
        return res
        