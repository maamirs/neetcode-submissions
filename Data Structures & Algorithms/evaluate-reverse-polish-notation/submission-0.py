class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = '+-/*'

        valuestack = []

        for c in tokens:
            if c in operators:
                val2 =  valuestack.pop()
                val1 =  valuestack.pop()
                finalval = 0
                if c == '+':
                    finalval = val1 + val2
                elif c == '-':
                    finalval = val1 - val2
                elif c == '*':
                    finalval = val1 * val2
                elif c == '/':
                    finalval = int (val1 / val2)
                
                valuestack.append(finalval)
            else:
                valuestack.append(int(c))
        

        return valuestack[0]
        