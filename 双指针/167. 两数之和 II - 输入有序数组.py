# 双指针
class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            sum_ = numbers[l] + numbers[r]
            if sum_ > target:
                r -= 1
            elif sum_ < target:
                l += 1
            else:
                return [l + 1, r + 1]

# 哈希表
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(numbers)):
            goal = target - numbers[i]
            if goal in hashMap:
                return [hashMap[goal] + 1, i + 1]
            else:
                hashMap[numbers[i]] = i