class Solution:
    def isValid(self, s: str) -> bool:
        top = [] * len(s)
        valid = False
        opening = ['(','[','{']
        closing = [')',']','}']
        for x in range(len(s)):
            if(s[x] in opening):
                top.append(s[x])
            if(s[x] in closing):
                if not len(top) > 0:
                    valid = False
                    break
                if len(top) > 0:
                    a = top.pop()
                    if opening.index(a) == closing.index(s[x]):
                        valid = True
                    else:
                        valid  = False
                        break
        if len(top) > 0:
            return False
        return valid
