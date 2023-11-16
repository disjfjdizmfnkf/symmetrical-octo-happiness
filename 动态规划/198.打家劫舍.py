########################################################################################################
#                                        得到最终答案的过程
#  1. 思考问题了解递归的过程     2.使用一般的递归解法    3.使用记忆优化递归
#  4. 将递归改为迭代           5.使用变量替代记忆(动态规划)
########################################################################################################

# 用递归理解动态规划
# 返回p之后可以强到的最大金额
class Solution1:
    def rob(self, nums: List[int]) -> int:
        def helper(nums, p):
            if p >= len(nums):
                return 0
            return max(nums[p] + helper(nums, p + 2), helper(p + 1))  # 画出决策树 只有抢和不抢当前的两种情况
        return helper(nums, 0)

# 递归 + 记忆 优化
class Solution2:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def helper(nums, p):
            if p >= len(nums):
                return 0
            if p in memo:
                return memo[p]
            memo[p] = max(nums[p] + helper(nums, p + 2), helper(p + 1))
            return memo[p]
        return helper(nums, 0)

# 迭代 + 记忆
# 使用数组来记录抢不抢当前位置的两种情况
class Solution3:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        memo[0], memo[1] = 0, nums[0]
        for i in range(len(nums)):
            memo[i + 1] = max(memo[i], memo[i - 1] + nums[i]) # memo[i]是不抢当前  memo[i - 1] + nums[i] 是抢当前
        return memo[len(nums)]

# 使用变量代替memo  动态规划
class Solution:
    def rob(self, nums: List[int]) -> int:
        rub1, rub2 = 0, 0

        # [rub1, rub2, n, n+1, ...]
        for n in nums:
            temp = max(rub1 + n, rub2)  # temp 为可偷到的最大金额 rub1 + n 为偷当前房子，rub2 为不偷当前房子 只有这两种情况
            rub1 = rub2
            rub2 = temp
        return rub2