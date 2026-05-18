class Solution:
    def isValid(self, s: str) -> bool:
        mydict = {')' : '(', '}' : '{', ']' : '['}

        stack = []

        for c in s:
            if c not in mydict:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != mydict[c]:
                        return False
        
        return not stack