class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        res = len(t)
        s_t = s
        i = 0
        while i < len(t) and i < len(s):
            if s[i] == t[i]:
                res -= 1
                i += 1
                continue
            s_t += t[i]
            i += 1
        return res
            


            
        