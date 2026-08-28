class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        best_profit=0
        for price in prices[1:]:
            min_price=min(min_price,price)
            profit = price-min_price
            best_profit=max(profit,best_profit)
        return best_profit
