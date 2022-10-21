class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        """
        1,2,3,4   p 2
        
        
        """
        tokens.sort()
        score = 0
        start,end = 0, len(tokens)-1
        
        while start <= end:
            
            if tokens[start] <= power:
                power -= tokens[start]
                score += 1
                start += 1
            else:
                if start < end and score > 0:
                    power += tokens[end]
                    end -= 1
                    score -= 1
                else:
                    return score
        return score