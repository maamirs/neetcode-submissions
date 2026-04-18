class Solution:
    def isValid(self, s: str) -> bool:

        mystack = []

        for c in s:
            if c in '({[':
                mystack.append(c)
            else:
                if not mystack:
                    return False  
                elif c == ']' and mystack[-1] == '[':
                    mystack.pop()
                elif c == '}' and mystack[-1] == '{':
                    mystack.pop()
                elif c == ')' and mystack[-1] == '(':
                    mystack.pop()
                else:
                    return False
            
        
        if mystack:
            return False
        
        return True
        