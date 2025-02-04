class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        memo = set(nums)
        res = 1
        while True:
            if res in memo:
                res += 1
            else:
                return res

class Solution2:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 将每个数放到正确的位置上
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # 找到第一个位置不正确的数
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1