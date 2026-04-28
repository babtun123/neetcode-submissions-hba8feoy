import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b) 
        }

        stack = []
        operands = ("*", "+", "-", "/")
        for num in tokens:
            if num in operands:
                num2 = stack.pop()
                num1 = stack.pop()
                res = ops[num](num1, num2)
                stack.append(res)
            else:
                stack.append(int(num))
        return stack[0]
