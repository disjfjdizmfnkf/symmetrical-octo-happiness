from typing import List
##################################################################################################

class Solution:
    # dp 记录离开前/到达该位置前/最小花费
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # 记录到达i位置的最小花费 意味着需要len(cost)这个额外的位置保存答案
        L = [0] * (len(cost) + 1)

        # 从位置2开始是因为前两个位置的最小花费(离开前)为默认值
        for i in range(2, len(cost) + 1):
        # 找子问题之间的关系 只需要看着图分析前几个 大脑知道这么计算最小花费 但是我需要抽象化这个过程及其细节
            L[i] = min(L[i - 1] + cost[i - 1], L[i - 2] + cost[i - 2])
        return L[-1]

    # 优化空间复杂度 意识到一直在使用L[i - 1] L[i - 2],可以用dp1 dp2 滚动更新代替
    def minCostClimbingStairs_(self, cost: List[int]) -> int:
        dp1, dp2 = 0, 0
        for i in range(2, len(cost) + 1):
            dp = min(dp1 + cost[i - 1], dp2 + cost[i - 2])
            dp2 = dp1
            dp1 = dp
        return dp

    # dp 记录从该位置离开的最小花费
    def minCostClimbingStairs_(self, cost: List[int]) -> int:
        L = [float('inf')] * len(cost)
        # 不要想初始化的这几个是怎样计算得到的，把正确的值赋值给它们就行
        # 需要想的最好是后面的子问题之间的关系
        L[0], L[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            L[i] = cost[i] + min(L[i - 1], L[i - 2])
        return min(L[-1], L[-2]) # L数组中值的含义是离开i位置的最小花费 我们也可以换一种写法，我们可以将cost最后，
                # 添加一个空位置值为0，因为最后我们不需要再计算离开的值了，创建的L长度再加一，返回最后一个位置的值

    # 上一种方法的空间优化

    # 没过

    # def minCostClimbingStairs_(self, cost: List[int]) -> int:
    #     dp1, dp2 = cost[0], cost[1]
    #     for i in range(2, len(cost)):
    #         dp = cost[i] + min(dp1, dp2)
    #         dp2 = dp1
    #         dp1 = dp
    #     return min(dp1, dp2)
