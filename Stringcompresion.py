class Solution:
    def compress(self, chars: List[str]) -> int:
        
        if len(chars) == 1: return 1
        
        l,r = 0,1
        count = 1
        s = []
        for x in range(len(chars)):
            if r < len(chars) and chars[l] == chars[r]:
                count += 1
                r += 1
            elif count == 1:
                s.append(chars[l])
                l = r
                r += 1
                count = 1
            else:
                s.append(chars[l])
                s.extend(str(count))
                l = r
                r += 1
                count = 1
        
        chars[:len(s)] = s
        return len(s)