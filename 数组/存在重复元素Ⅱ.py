# HashMap 利用哈希表的特性，当添加的key重复时，覆盖对应的value
# 没有思路时应该画图，因为要在一定的范围内找，刚好配合哈希表的特性，同一个key可以覆盖赋值
# 这样从左往右遍历时就可以保证hash表中的value和与它相等的数字是最近的
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}
        for index, num in enumerate(nums):
            if num not in hashMap:
                hashMap[num] = index
            else:
                if abs(hashMap[num] - index) <= k:
                    return True
                else:
                    hashMap[num] = index
        return False
