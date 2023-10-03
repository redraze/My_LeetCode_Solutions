class Solution:
    def isValid(self, s: str) -> bool:
        open = set()
        open.add('(')
        open.add('[')
        open.add('{')
        closed = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for ch in s:
            if ch in open:
                stack.append(ch)
                continue
            if stack == [] or stack[-1] != closed[ch]:
                return False
            stack.pop()
        if stack == []:
            return True
        return False
