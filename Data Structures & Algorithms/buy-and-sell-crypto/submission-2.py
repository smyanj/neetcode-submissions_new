class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        minV = prices[l]

        while r < len(prices):
            minV = min(minV, prices[l])
            currPrice = prices[r] - minV
            if currPrice > maxProfit:
                maxProfit = currPrice
            
            l += 1
            r += 1

        return maxProfit