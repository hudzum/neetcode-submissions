class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hp = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] > prices[l]:
                hp = max(hp, prices[r]-prices[l])
            else:
                l = r
            r+=1

        return hp
            
