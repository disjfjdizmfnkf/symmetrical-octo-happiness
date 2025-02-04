class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        输入: nums = [0,1,0,3,12]
        输出: [1,3,12,0,0]
        """

        # 将非零的数都移动到左边(双指针)，最后将慢指针后面的都清零
        if not nums:
            return
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j] = nums[i]
                j += 1
        for j in range(j, len(nums)):
            nums[j] = 0 