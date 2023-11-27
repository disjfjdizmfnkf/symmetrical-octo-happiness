
# 把这个当作贪心问题更好理解， 如果看作是动态规划，那么就是一个一维的动态规划，
# 那么问题就是以d[i]结尾的的最大子序和

# 动态规划 时间复杂度O(n)  空间复杂度O(1)
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]           # 数组中有负数，best不一定为0
        now = 0
        for i in nums:
            if now < 0:  # 当前和为负数，一定不包含在之后的最大连续数组内
                now = 0
            now += i
            best = max(best, now) # 更快的写法: if best < now : best = now
        return best




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
