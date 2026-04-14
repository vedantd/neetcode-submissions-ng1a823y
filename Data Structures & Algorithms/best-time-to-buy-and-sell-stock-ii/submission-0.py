class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minima = float("inf")
        profit = 0
        for i in range(len(prices)-1):
            if prices[i] < minima:
                minima = prices[i]
                
            
            if prices[i] < prices[i+1]:
                profit = profit + (prices[i+1] - prices[i])
            
        return profit



        