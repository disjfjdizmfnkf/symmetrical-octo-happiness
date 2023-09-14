#返回数组中超出数组元素个数一半的元素

# hashMap 时间复杂度O(n)
class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = dict()
        threshold = len(nums)//2
        for i in nums:
            hashMap[i] = hashMap.get(i, 0) + 1
            if hashMap[i] > threshold:
                return i
        
# Boyer-Moore 投票算法  摩尔投票算法
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        cand_num = nums[0]
        count = 1
        for i in nums:
          if i == cand_num:
            count += 1
          else:
            count -= 1
            if count == 0:
              cand_num = i
              count = 1
        return cand_num


# 先排序再看 时间复杂度O(nlogn)
class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n%2 == 0:
            return nums[n//2 - 1] #可以想象一个滑块在一个槽里滑动，滑块的长度>=槽的一半
        return nums[n//2]

    