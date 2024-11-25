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

    # 优化为一行数组
    def canPartition(self, nums: List[int]) -> bool:
        """
        dp[i][j] 前i个数可否构成和为j的数组
        状态转移方程 dp[i][j] = dp[i-1][j-x] | dp[i-1][j]
        求dp[i][j] 因为依赖于i-1层的[i-1][j-x]和[i-1][j] 
        所以优化为一维数组时前面的值不能变，需要从后往前更新
        i-1   [o]       [o]
        i     [o]       [x]
              j-x  ...   j    
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [False] * (target + 1)  # 给0预留一个位置
        dp[0] = True
        
        for num in nums:
            # j < x 时没有意义 num构成的数不能比num小
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target]
