class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        top = []
        value = 0
        operator = ['+','-','*','/']
        for x in range(len(tokens)):
            if not tokens[x] in operator:
                top.append(tokens[x])
            else:
                if tokens[x] == '+':
                    value = int(top.pop())
                    top.append(int(top.pop()) + value)
                elif tokens[x] == '-':
                    value = int(top.pop())
                    top.append(int(top.pop()) - value)
                elif tokens[x] == '*':
                    value = int(top.pop())
                    top.append(int(top.pop()) * value)
                elif tokens[x] == '/':
                    value = int(top.pop())
                    top.append(int(top.pop()) / value)
                    
        return int(top[0])
                