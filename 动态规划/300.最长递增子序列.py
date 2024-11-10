from typing import List


class Solution:
    def lengthOfLIS0(self, nums: List[int]) -> int:
        n = len(nums)
        dp, ans = [1] * n, 0
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])
        return ans


    def lengthOfLIS1(self, nums: List[int]) -> int:
        # 为问题作图分析
        # 找到子问题
        # 找到子问题之间的关系

        # 可视化后 想到借助列表存储解决问题
        L = [1] * len(nums)  # 最小递增子列表的长度为1
        for i in range(1, len(nums)):
            sub_problem = [L[k] for k in range(i) if nums[k] < nums[i]]  # 寻找子问题
            L[i] = 1 + max(sub_problem, default=0)  # 子问题之间的关系
        return max(L, default=0)
