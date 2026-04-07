class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        clear = "".join([char for char in s if char.isalnum()])
        r = len(clear) - 1

        while l < r:
            if clear[l].lower() == clear[r].lower():
                l += 1
                r -= 1
                continue
            return False

        
        return True
