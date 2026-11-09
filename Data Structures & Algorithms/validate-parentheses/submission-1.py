class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {"(": ")", "{": "}", "[": "]"}

        for i in range(0, len(s)):
            if s[i] in ["(", "{", "["]:
                stack.append(s[i])
            elif stack and bracketMap[stack[-1]] == s[i]:
                stack.pop()
            else:
                return False

        return len(stack) == 0
        