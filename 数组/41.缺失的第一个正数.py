class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        memo = set()
        res = 1
        for num in nums:
            if num > 0:
                memo.add(num)
        while True:
            if res in memo:
                res += 1
            else:
                break
        return res
