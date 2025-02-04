

# 方法一: 寻找所有可能的连续子区间
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        best, subSum = nums[0], 0           # 数组中有负数，best不一定为0
        for i in nums:  # 寻找所有区间, 更新最优区间
            if subSum < 0:  # 如果前面的和小于0，那么对后面的和没有增益，直接舍弃
                subSum = 0
            subSum += i
            best = max(best, subSum) # 更快的写法: if best < now : best = now
        return best



# 方法二: 前缀和数组求区间  连续子数组 -> 区间 -> 利用前缀和数组
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n): nums[i] += nums[i - 1]  # 前缀和数组
        # 如果将pre_min初始化为nums[0]会导致第一个位置的最大前缀和永远计算为0
        pre_min = 0  # 刚开始最小前缀和为0
        ans = nums[0]  # 初始化为第一个数字
        for i in nums:
            ans = max(ans, i - pre_min)
            pre_min = min(pre_min, i)
        return ans





# 没掌握
# 分治法 时间复杂度O(nlogn)  空间复杂度O(logn)
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(nums, l, r):
            if l == r:
                return nums[l]
            mid = (l + r) // 2
            left = helper(nums, l, mid)
            right = helper(nums, mid + 1, r)
            # 跨越中点的最大子序列
            leftMax = nums[mid]
            now = 0
            for i in range(mid, l - 1, -1):
                now += nums[i]
                leftMax = max(leftMax, now)
            rightMax = nums[mid + 1]
            now = 0
            for i in range(mid + 1, r + 1):
                now += nums[i]
                rightMax = max(rightMax, now)
            return max(left, right, leftMax + rightMax)
        return helper(nums, 0, len(nums) - 1)
