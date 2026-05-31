

#        r     
# coaching
#   l
# coding

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l, r = 0, 0
        res = len(t)

        while r < len(s) and l < len(t):
            if t[l] == s[r]:
                res -= 1
                r += 1
                l += 1
                continue
            r += 1

        return res
            


            
        