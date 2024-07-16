class Solution:

    # 使用二维数组
    def canPartition0(self, nums: List[int]) -> bool:
        # dp[i][j] 前i个数可否构成和为j的数组
        # 状态转移方程 dp[i][j] = dp[i-1][j-x] | dp[i-1][j]
        # 我从哪里来： dp[i][j] 是否使用第i个数
        n, total = len(nums), sum(nums)
        if total % 2:
            return False
        dp = [[0] * (total + 1) for _ in range(n + 1)]
        dp[0][0], accumulate = 1, 0
        for i in range(1, n + 1):
            accumulate += nums[i - 1]
            for j in range(accumulate + 1):
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
        return bool(dp[-1][total//2])

    # 一行一维数组
    def canPartition(self, nums: List[int]) -> bool:
        n, total = len(nums), sum(nums)
        if total % 2: return False
        dp = [0] * (total + 1)
        dp[0], accumulate = 1, 0
        for x in nums:
            accumulate += x
            for j in range(accumulate, x - 1, -1):
                dp[j] |= dp[j - x]
        return bool(dp[total//2])

    # 使用滚动数组  有错
    def canPartition1(self, nums: List[int]) -> bool:
        n, total = len(nums), sum(nums)
        if total % 2:
            return False
        dp = [[0] * (total + 1) for _ in range(2)]
        dp[0][0], accumulate = 1, 0
        for i in range(1, n):
            accumulate += nums[i - 1]
            ind = i % 2
            pre = not ind
            for j in range(accumulate + 1):
                dp[ind][j] = dp[pre][j] or dp[pre][j - nums[i - 1]]
        return bool(dp[-1][total//2])




