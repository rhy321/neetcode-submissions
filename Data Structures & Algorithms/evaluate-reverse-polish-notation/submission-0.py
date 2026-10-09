class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for c in tokens:
            if c == "+":
                a, b = stk.pop(), stk.pop()
                stk.append(b + a)
            elif c == "-":
                a, b = stk.pop(), stk.pop()
                stk.append(b - a)
            elif c == "*":
                a, b = stk.pop(), stk.pop()
                stk.append(b * a)
            elif c == "/":
                a, b = stk.pop(), stk.pop()
                stk.append(int(b / a))
            else:
                stk.append(int(c))

        return stk[-1]