#https://www.youtube.com/watch?v=1pkOgXD63yU&t=21s
#https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150




#双指针 动态规划  一个(为最高点)遍历所有点，一个越来越低找最低点
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else:  #如果不是prices[l] < prices[r]的话，说明现在的r位置价格更低
                l = r
            r += 1
        return maxP