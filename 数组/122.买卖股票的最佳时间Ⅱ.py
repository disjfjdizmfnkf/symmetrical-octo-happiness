"""给你一个整数数组 prices ，其中 prices[i]表示某支股票第 i 天的价格。
在每一天,你可以决定是否购买和/或出售股票。你在任何时候最多只能持有 一股股票。
你也可以先购买，然后在同一天出售.返回你能获得的最大利润

输入：prices = [7,1,5,3,6,4]
输出：7
解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3 。
     总利润为 4 + 3 = 7 。

"""

#窗口滑动   把所有向上增长的一段一段加起来
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])
        return profit