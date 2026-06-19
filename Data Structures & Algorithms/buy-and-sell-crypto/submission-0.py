class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hp = 0 
        for i, b in enumerate(prices):
            for s in range(i+1, len(prices)):
                hp = max(hp, prices[s]-b)
        return hp