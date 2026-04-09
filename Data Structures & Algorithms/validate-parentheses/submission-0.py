class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if not s:
            return True

        for c in s:
            if c in "([{":
                stack.append(c)
            
            if c in "}])":
                stack.pop()
        
        if not stack:
            return True
        return False
