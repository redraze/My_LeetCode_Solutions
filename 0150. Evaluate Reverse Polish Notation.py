class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                first = int(stack.pop())
                second = int(stack.pop())
                stack.append(first + second)
            elif token == '-':
                first = int(stack.pop())
                second = int(stack.pop())
                stack.append(second - first)
            elif token == '*':
                first = int(stack.pop())
                second = int(stack.pop())
                stack.append(first * second)
            elif token == '/':
                first = int(stack.pop())
                second = int(stack.pop())
                stack.append(int(second/first))
            else:
                stack.append(int(token))
        return stack[-1]
