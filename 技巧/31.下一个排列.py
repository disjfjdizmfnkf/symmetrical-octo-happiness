class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 从后往前找nums[k] < nums[k+1]
        for k in range(n - 2, -1, -1):
            if nums[k] < nums[k + 1]:
                break
        # 这里的else只有在for循环正常结束后才会执行，执行break会跳过else执行
        else:
            return nums.reverse()
        
        # eg.[4, 2, 3, 1] 从后往前找到第一个nums[l] > nums[k]的位置 3， 2
        for i in range(n - 1, k - 1, -1):
            if nums[i] > nums[k]:
                break

        # 交换nums[l] nums[k]
        nums[i], nums[k] = nums[k], nums[i]

        # 反转k+1到末尾的部分
        nums[k+1:]  = nums[k+1:][::-1]        