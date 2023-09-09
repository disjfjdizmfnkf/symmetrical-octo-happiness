
# 快慢指针，一个负责前部分返回的元素，一个在后半访问元素

class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0
        while(fast < len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow = slow + 1
            fast = fast + 1
        return slow

