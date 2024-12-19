

# 贪心算法 第二次写
class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dis = nums[0]
        # 计算最远跳跃距离
        for i in range(n):
            if i <= dis:
                dis = max(dis, i + nums[i])
            else:
                break
        if dis + 1 >= n:  # 索引是从0开始的，这个长度是1 需要计算在内
            return True
        return False
