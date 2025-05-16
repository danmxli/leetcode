class Solution:
    def isValid(self, s: str) -> bool:
        parens = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        stack = []
        for c in s:
            if c in parens:
                stack.append(c)
            else:
                if not stack:
                    return False
                # pythonic stack peek
                if parens[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        return True
    
sol = Solution()
print(sol.isValid("([])"))