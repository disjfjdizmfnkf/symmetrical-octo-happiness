class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 方法：先确定一个数，在它之后的范围中再找两个数，使得三者的和为0

        result = []
        nums.sort()  # 先对数组进行排序

        for i in range(len(nums) - 2):
            # 两个相邻的相同的数，如果前者匹配到一个数组，那么后者大概率会匹配到相同的数组（不是一定，有特殊情况）
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # 避免数组中的第二/三位 和之前的数组重复
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result