
# 把这个当作贪心问题更好理解， 如果看作是动态规划，那么就是一个一维的动态规划，
# 那么问题就是以d[i]结尾的的最大子序和

# 动态规划 时间复杂度O(n)  空间复杂度O(1)
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        best, sum_ = nums[0], 0           # 数组中有负数，best不一定为0
        for i in nums:
            if sum_ < 0:
                sum_ = 0
            sum_ += i
            # if now < 0:  写在这个位置会修改掉原始结果
            #     now = 0
            best = max(best, sum_) # 更快的写法: if best < now : best = now
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
