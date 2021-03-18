# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
class Solution:
    def maxProfit(self, prices, fee):
        sell=0
        hold=-prices[0]
        for i in range(1,len(prices)):
            sell=max(sell, hold+prices[i]-fee)
            hold=max(hold, sell-prices[i])
        return sell
        