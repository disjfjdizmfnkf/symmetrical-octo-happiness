
#
class Solution1:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        count = 0

        while r < len(nums) - 1:  # 下标
            maxDis = 0
            for i in range(l, r + 1):
                maxDis = max(maxDis, i + nums[i])
            count += 1
            l = r + 1
            r = maxDis
        return count

# 贪心
class Solution2:
    def jump(self, nums: List[int]) -> int:
        jumpCount, curEnd, curFarthest = 0, 0, 0
        for i in range(len(nums) - 1):
            curFarthest = max(curFarthest, i + nums[i])
            if i == curEnd:
                jumpCount += 1
                curEnd = curFarthest
        return jumpCount