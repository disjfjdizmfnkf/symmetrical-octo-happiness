#返回数组中超出数组元素个数一半的元素

# hashMap 时间复杂度O(n)
class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hashMap = {}
        for i in nums:
            count = hashMap.get(i, 0)
            if count > n // 2:
                return i
            hashMap[i] = count + 1

# Boyer-Moore 投票算法 摩尔投票算法
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        hold, count = 0, 0
        for n in nums:
            if count == 0:
                hold = n
            count += (1 if n == hold else -1)
        return hold

# 先排序再看 时间复杂度O(nlogn)
class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n%2 == 0:
            return nums[n//2 - 1] #可以想象一个滑块在一个槽里滑动，滑块的长度>=槽的一半
        return nums[n//2]

    