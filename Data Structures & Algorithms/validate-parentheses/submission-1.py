class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {")": "(", "]": "[", "}": "{"}
        if not s:
            return True

        for c in s:
            if c in "([{":
                stack.append(c)
                continue
            
            if matches[c] == stack[-1] and stack:
                stack.pop()
        
        if not stack:
            return True
        return False
