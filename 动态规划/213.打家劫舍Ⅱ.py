class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0][0], dp[0][1] = 0, nums[0]

        dp[1][0], dp[1][1] = 0, nums[1]
        for i in range(1, n + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i - 1]
        ans1 = dp[n - 1][0]
        dp[1][0] = dp[1][1] = 0
        for i in range(1, n + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i-1][1])
            dp[i][1] = dp[i - 1][0] + nums[i - 1]
        ans2 = max(dp[n - 1][0], dp[n - 1][1])
        return max(ans1, ans2)