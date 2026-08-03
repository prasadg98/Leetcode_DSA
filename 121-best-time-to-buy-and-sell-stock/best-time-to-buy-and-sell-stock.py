class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = 0
        for right in range(1,len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                diff = prices[right] - prices[left]
                profit = max(profit, diff)
        
        if profit == 0:
            return 0
        else:
            return profit