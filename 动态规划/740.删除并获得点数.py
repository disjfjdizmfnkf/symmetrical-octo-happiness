class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))

        # [3, 4, 2]
        # [0, 0, 0]
        dp1, dp2 = 0, 0
        for i in range(len(nums)):
            curEarn = nums[i] * count[nums[i]]
            if i > 0 and nums[i] - nums[i - 1] == 1:
                temp = dp2
                dp2 = max(curEarn + dp1, dp2)
                dp1 = temp
            else:
                temp = dp2
                dp2 = curEarn + dp2
                dp1 = temp
        return dp2
