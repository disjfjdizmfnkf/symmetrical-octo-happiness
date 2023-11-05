

# 贪心算法 第二次写
class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        dis = 0
        for i in range(len(nums)):
            if i <= dis:  # i必须满足在能跳跃的范围内跳
                dis = max(i + nums[i], dis)
        if dis >= len(nums) - 1:
            return True
        return False


# 改变遍历范围
class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        dis = 0   # 记录此时可以达到的最远距离
        for i in range(len(nums)):  # 为什么不能直接把范围改成 range（dis）
            if i > dis:  #  i一定在此时能到的最大范围内
                break
            dis = max(dis, i + nums[i])
            if dis >= len(nums) - 1:
                return True
        return False

