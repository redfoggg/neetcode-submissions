class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sTot = {}

        for i in range(len(s)):
            if s[i] in sTot and t[i] != sTot[s[i]]:
                return False
            sTot[s[i]] = t[i]
        return True
        