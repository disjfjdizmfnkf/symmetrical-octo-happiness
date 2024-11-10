
# 双指针
class Solution:
    def maxArea(self, height: List[int]) -> int: # 越宽越高 越好
        # 宽度 当然越宽越好
        l, r = 0, len(height) - 1
        best = 0
        # 在宽度缩小时，只有舍弃短边去寻找可能的长边才是有意义的
        while l < r:
            best = max(best, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return best