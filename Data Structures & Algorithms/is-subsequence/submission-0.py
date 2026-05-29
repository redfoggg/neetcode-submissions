class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t) or len(t) == 0:
            return False
        if len(s) == 0:
            return True
        count = 0
        lastOcurrency = 0
        for i in range(len(s)):
            for j in range(lastOcurrency ,len(t)):
                if s[i] == t[j]:
                    count += 1
                    lastOcurrency = j

        return count == len(s)
                

            


        
        
        