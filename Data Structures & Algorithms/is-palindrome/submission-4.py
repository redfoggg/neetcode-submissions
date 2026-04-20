class Solution:
    def isPalindrome(self, s: str) -> bool:
        sn = [c.lower() for c in s if c.isalnum()]
        l, r = 0, len(sn) - 1

        while l < r:
            cl = sn[l]
            cr = sn[r]
            if cl == cr:
                l += 1
                r -= 1
            else:
                return False

        return True
        