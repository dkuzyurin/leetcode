# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        propen = ('(', '[', '{')
        prclose = (')', ']', '}')
        stack = []
        for sym in s:
            if sym in propen:
                stack.append(sym)
                continue
            ind = prclose.index(sym)
            if not len(stack):
                return False
            prev = stack.pop()
            if prev not in propen or propen.index(prev) != ind:
                return False
        return len(stack) == 0
    
s = Solution()
print(s.isValid("{[]}("))