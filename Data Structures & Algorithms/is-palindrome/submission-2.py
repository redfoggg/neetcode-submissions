class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        clear = "".join(char.lower() for char in s if char.isalnum())
        r = len(clear) - 1

        while l < r:
            if clear[l] != clear[r]:
                return False
            l += 1
            r -= 1

        
        return True
