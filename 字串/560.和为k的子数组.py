class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        # 记录此时之前的前缀和的出现次数
        countPrefix = {0:1}
        res = 0
        for num in nums:
            prefixSum += num
            # 先计算之前满足要求的子数组，否则会出错 eg. nums:[] k:1
            if prefixSum - k in countPrefix:
                res += countPrefix[prefixSum - k]
            # 之后再将这个加入count计数
            countPrefix[prefixSum] = countPrefix.get(prefixSum, 0) + 1
        return res
