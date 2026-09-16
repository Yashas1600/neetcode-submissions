class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '-', '*', '/'}
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                y = stack.pop()
                x = stack.pop()

                if token == '+':
                    stack.append(x + y)
                elif token == '-':
                    stack.append(x - y)
                elif token == '*':
                    stack.append(x * y)
                else:
                    stack.append(int(x/y))

        return stack.pop()        