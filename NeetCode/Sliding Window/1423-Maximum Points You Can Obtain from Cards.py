class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l, r = 0, len(cardPoints) - k
        total = sum(cardPoints[r:])
        res = total

        for i in range(k):
            total += (cardPoints[l + i] - cardPoints[r + i])
            res = max(res, total)
        return res