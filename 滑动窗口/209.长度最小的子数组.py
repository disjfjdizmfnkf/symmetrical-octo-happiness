

# 滑动窗口
class Solution1:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float("inf")
        for r in range(len(nums)):  # 右边指针只顾往前走
            total += nums[r]  # 向左边滑动增大值
            while total >= target:  # 满足条件了，我们尝试去找到最小窗口
                res = min(r - l + 1, res)
                total -= nums[l] # 向右边滑动减小值
                l += 1
        return 0 if res == float("inf") else res