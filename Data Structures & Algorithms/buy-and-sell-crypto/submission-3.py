class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestprice = prices[0]
        bestprof = 0

        for sell in prices:
            bestprof = max(bestprof, sell-lowestprice)

            lowestprice = min(lowestprice, sell)

        return bestprof
            
