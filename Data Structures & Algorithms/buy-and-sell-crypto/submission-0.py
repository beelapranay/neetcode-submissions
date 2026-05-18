class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        minPrice = float('inf')
        maxProfit = 0

        while (i < len(prices)):
            if (prices[i] < minPrice):
                minPrice = prices[i]

            currProfit = prices[i] - minPrice
            maxProfit = max(maxProfit, currProfit)
            i+=1

        return maxProfit        