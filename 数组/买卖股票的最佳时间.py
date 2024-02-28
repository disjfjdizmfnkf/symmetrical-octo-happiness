#动态规划  一个(为最高点)遍历所有点，一个越来越低找最低点
class Solution:
    # method: 从左往右计算所有利润(并且以之前的最低价买入)
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit = 0
        for p in prices:
            if p > low:
                profit = max(profit, p - low)
            else:
                low = p
        return profit