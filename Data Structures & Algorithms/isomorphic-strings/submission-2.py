class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sTot = {}
        tTos = {}

        for i in range(len(s)):
            if s[i] in sTot and t[i] != sTot[s[i]]:
                return False
            sTot[s[i]] = t[i]
        
        for i in range(len(t)):
            if t[i] in tTos and s[i] != tTos[t[i]]:
                return False
            tTos[t[i]] = s[i]

        return True
        