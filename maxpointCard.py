class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l,r = 0,len(cardPoints) - k
        
        total = sum(cardPoints[r:])
        ans = total
        while r < len(cardPoints):
            total += (cardPoints[l] - cardPoints[r])
            ans = max(ans,total)
            l += 1
            r += 1
        return ans