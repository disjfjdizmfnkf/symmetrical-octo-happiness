class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 方法：先确定一个数，在它之后的范围中再找两个数，使得三者的和为0

        result = []
        nums.sort()  # 先对数组进行排序

        for i in range(len(nums) - 2):
            # 如果后面的数字和前面的数字重复就跳过这些数字, 
            # 跳过重复的数字 注意防止越界 if nums[i] == nums[i + 1]:
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                _sum = nums[i] + nums[left] + nums[right]
                if _sum < 0:
                    left += 1
                elif _sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # 跳过重复数字
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result
