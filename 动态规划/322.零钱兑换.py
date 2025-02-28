# 自下而上的动态规划dp
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 从哪里来: 当前金额的最少硬币数是由之前金额的最少硬币数 + 一枚硬币得到的
        dp = [amount + 1] * (amount + 1)  # 金额是从0开始
        dp[0] = 0
        for i in range(amount + 1):
            for v in coins:
                if i >= v:
                    dp[i] = min(dp[i - v] + 1, dp[i])
        return dp[-1] if dp[-1] != amount + 1 else -1  # 无法兑换的还会是初始值

    def coinChange0(self, coins: List[int], amount: int) -> int:
        L = [amount + 1] * (amount + 1)
        L[0] = 0  # 0元需要0个硬币
        for i in range(1, amount + 1):  # 注意范围
            for coin in coins:
                if i - coin >= 0:  # find sub_problem
                    L[i] = min(1 + L[i - coin], L[i])  # 在子问题中挑选最优解
        return L[amount] if L[amount] != amount + 1 else -1

    def coinChange1(self, coins: List[int], amount: int) -> int:
        # dp[i]总金额为i时所需要的最少硬币数
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i < coin:
                    continue
                if dp[i - coin] == -1:
                    continue
                # dp[i]: 当前不使用该coin时的最小硬币数 dp[i-coin] + 1:使用当前coin后的最小硬币数
                if dp[i] == -1 or dp[i] > dp[i - coin] + 1:
                    dp[i] = dp[i - coin] + 1
        return dp[-1]

    # dp[amount] 为默认值 amount + 1 最大
    def coinChange2(self, coins: List[int], amount: int) -> int:
        L = [amount + 1] * (amount + 1)
        L[0] = 0  # 0元需要0个硬币
        for i in range(1, amount + 1):
            sub_problem = [L[i - k] for k in coins if i - k >=
                           0 and L[i - k] != amount + 1]  # 找到所有有效的子问题
            if sub_problem:
                L[i] = min(sub_problem) + 1
        return -1 if L[amount] == amount + 1 else L[amount]


# 位运算 看看得了

############## 位运算 ####################
# 位运算的思路：将 1 向左移 amount 位
# 然后根据 coins，不断地向右移，直到 1 回到最后一位。这样做的好处是：
# 向右移几位，表示用了多少的 coins，比如：1000 变成 111 表示
# amount = 3，所以将 1 左移三位变成 1000。111 说明向右移动了三次
# 分别是一次：100，两次 10，三次 1，最后通过 bitwise_or 将三次结果合一
# 观察 1000 和 111，我们通过 coins，不断地右移， 将原本向左移动了三位的 1，
# 现在又移动到了末尾，说明我们已经还原。也就是找到了最少使用硬币的方案。

# 另外对于重复的计算，bitwise_or 运算也不会留下痕迹。比如上一轮 coins 遍历完，
# 得到 110，下一轮继续遍历，得到 11，而 110 | 11 = 111，其中第二位有两个 1，
# 代表的是我们第一次时候 coins 的时候，往右移动两位，相当于第一次移动一位，
# 第二次在移动一位，也就是说，第一次用 2 的硬币，相当于第一次用 1 的硬币，
# 第二次也用 1 的硬币，直接剪枝

# 对于负数也有考虑，如果 amount - coin < 0，则通过右移的规则，最后一位为 0
# 而不为 1，因此直接排除了这种可能
class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        dp = 1 << amount
        for i in range(amount // min(coins)):
            tmp = 0
            for c in coins:
                tmp |= dp >> c
                if tmp & 1:
                    return i + 1
            dp = tmp
        return -1
