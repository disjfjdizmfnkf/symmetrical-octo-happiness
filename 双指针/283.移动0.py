class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
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