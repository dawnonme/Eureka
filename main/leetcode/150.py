class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def parse_operator(op):
            if op == '+':
                return lambda x, y: x + y
            elif op == '-':
                return lambda x, y: x - y
            elif op == '*':
                return lambda x, y: x * y
            elif op == '/':
                return lambda x, y: x // y if x ^ y >= 0 \
                                           else -int(-(x / y))
            return lambda x, y: None

        stack = []
        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                func = parse_operator(token)
                res = func(op1, op2)
                stack.append(res)
        return stack[0]