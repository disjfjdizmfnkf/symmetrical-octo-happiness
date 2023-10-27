

# 动态规划 时间复杂度O(n)  空间复杂度O(n)
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]   # 容易出错，想想为什么不设置为0             数组中有负数
        nowSub = nums[0]

        for n in nums:
            if nowSub < 0:
                nowSub = 0
            nowSub += n
            maxSub = max(maxSub, nowSub)
        return maxSub

# 动态规划 时间复杂度O(n)  空间复杂度O(1)
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]   # 容易出错，想想为什么不设置为0             数组中有负数
        nowSub = nums[0]

        for n in nums:
            nowSub = max(nowSub + n, n)
            maxSub = max(maxSub, nowSub)
        return maxSub



# 没掌握
# 分治法 时间复杂度O(nlogn)  空间复杂度O(logn)
class Solution3:
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
