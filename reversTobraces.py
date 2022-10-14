class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        
        """
        oc     ans = ans[::-1]
               ans = top.pop() + ans
        et   ans = top.pop() + ans etco
             ans = ans[::-1]
             octe
             top.pop() + ans octeel
             edocteel
        ed
        
        uevoli
        ""
        """        
        top = []
        ans = ""
        for x in s:
            if x == '(':
                top.append(ans)
                ans = ''
            elif x ==')':
                ans = ans[::-1]
                ans = top.pop() + ans
            else:
                ans += x
        return ans