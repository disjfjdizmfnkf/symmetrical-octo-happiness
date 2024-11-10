
# 快慢指针，一个在前面选择元素，一个在后只管覆盖

class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0
        while(fast < len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow = slow + 1
            fast = fast + 1  #nums[fast]等于val时，跳过这个位置
        return slow

