class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums))) # 去重

        # [3,  4,  2]
        # dp1 dp2
        # [3,  0,  0]

        # dp1, dp2 = 0, 0
        # for i in range(len(nums)):
        #     if i > 0 and nums[i] - nums[i - 1] == 1:
        #         temp = dp2
        #         dp2 = max(nums[i] * count[nums[i]] + dp1, dp2)
        #         dp1 = temp
        #     else:
        #         temp = dp2
        #         dp2 = nums[i] * count[nums[i]] + dp1
        #         dp1 = temp
        # return dp2

        L = [0] * (len(nums) + 1)
        L[1] = nums[0] * count[nums[0]]

        for i in range(2, len(nums) + 1): # 已经将L[0]和L[1]初始化了，所以从2开始遍历dp的列表
            if nums[i - 1] - nums[i - 2] == 1:
                L[i] = max(L[i - 2] + (nums[i - 1] * count[nums[i - 1]]), L[i - 1])
            else:
                L[i] = nums[i - 1] * count[nums[i - 1]] + L[i - 1]

        return L[-1]