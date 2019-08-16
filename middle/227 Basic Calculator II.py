class Solution:
    def calculate(self, s: str) -> int:
        def precedence(op):
            if op == '*' or op == '/':
                return 2
            else:
                return 1

        def cal(op, op1, op2):
            if op == '*':
                return op1 * op2
            elif op == '/':
                return op1 / float(op2)
            elif op == '+':
                return op1 + op2
            else:
                return op1 - op2

        opstack = []
        operands = []
        idx = 0
        for i in range(idx, len(s)):
            if s[i] in '+-*/':
                operands.append(s[idx:i])
                while len(opstack) > 0 and precedence(s[i]) <= precedence(opstack[-1]) \
                    and len(operands) >= 2:
                    op = opstack.pop()
                    op2 = int(operands.pop())
                    op1 = int(operands.pop())
                    res = cal(op, op1, op2)
                    operands.append(res)
                opstack.append(s[i])
                idx = i + 1
        operands.append(s[idx:])

        while opstack:
            op = opstack.pop()
            op2 = int(operands.pop())
            op1 = int(operands.pop())
            res = cal(op, op1, op2)
            operands.append(res)

        return int(operands[0])

