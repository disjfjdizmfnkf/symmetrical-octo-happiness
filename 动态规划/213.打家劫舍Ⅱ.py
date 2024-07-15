from typing import List


# 将环形问题可以转换成线性问题
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:  return nums[0]
        dp = [[0] * 2 for _ in range(n + 1)]

        # 不偷第一家
        dp[1][0], dp[1][1] = 0, 0
        for i in range(2, n + 1):  # 从第二间房子开始   我从哪里来 偷第i家和不偷第i家从哪里来
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i - 1]
        ans1 = max(dp[-1][0], dp[-1][1])

        # 不偷最后一家
        dp[1][0], dp[1][1] = 0, nums[0]
        for i in range(2, n + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i - 1]
        ans2 = dp[-1][0]

        return max(ans1, ans2)
