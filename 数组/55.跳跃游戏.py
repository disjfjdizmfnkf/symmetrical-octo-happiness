

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

# 改变遍历范围(不行)
class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        i = dis = 0   # 记录此时可以达到的最远距离
        while i < len(nums): # for i in range(len(nums)): 会立即生成一个不可变的序列
            if i > dis:  #  i一定在此时能到的最大范围内
                break
            dis = max(dis, i + nums[i])
            if dis >= len(nums) - 1:
                return True
            i += 1
        return False