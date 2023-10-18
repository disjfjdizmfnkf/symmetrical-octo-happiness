
#DFS
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
            r = farthe
        return jumpCount

# 贪心
class Solution2:
    def jump(self, nums: List[int]) -> int:
        curEnd, curFarthest, jumpCount = 0, 0, 0
        for i in range(len(nums) - 1):  # 减一避免当最后一个是curend之后还加1
            curFarthest = max(curFarthest, i + nums[i])
            if i == curEnd:  # it's time to jump
                jumpCount += 1
                curEnd = curFarthest
        return jumpCount