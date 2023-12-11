class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 为问题作图分析
        # 找到子问题
        # 找到子问题之间的关系

        # 可视化后 想到借助列表存储解决问题
        L = [1] * len(nums)# 最小递增子列表的长度为1
        for i in range(1, len(nums)):
            sub_problem = [L[k] for k in range(i) if nums[k] < nums[i]]  # 寻找子问题
            L[i] = 1 + max(sub_problem, default=0)  # 子问题之间的关系
        return max(L, default=0)
