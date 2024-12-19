
# DFS
class Solution1:
    """我觉得像一种横向的深度优先搜素"""

    def jump(self, nums: List[int]) -> int:
        jumpCount = 0
        l, r = 0, 0
        while r < len(nums) - 1:  # 下标并且到最后也不用跳了不跳就不执行函数
            farthest = 0
            for i in range(l, r + 1):   # 注意range不包含最后一个
                farthest = max(farthest, i + nums[i])
            jumpCount += 1
            l = r + 1
            r = farthest
        return jumpCount

# 贪心
class Solution2:
    # 在每个阶段中只跳跃最远的距离
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumpBorder, farthest, state = 0, 0, 0
        for i in range(n - 1):  # 不包含最后一个的索引
            # 寻找最大距离
            farthest = max(i + nums[i], farthest)
            if i == jumpBorder:  # 到达当前可达距离的边界
                state += 1
                jumpBorder = farthest
        return state