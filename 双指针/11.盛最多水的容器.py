
# 双指针

# 一开始宽度最大，所以只有为两个边找更高的边界才有意义
class Solution1:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        best = (r - l) * min(height[r], height[l])
        while l < r:
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            water = (r - l) * min(height[r], height[l])
            best = max(best, water)
        return best

# 优化过后
class Solution2:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        best = (r - l) * min(height[r], height[l])
        while l < r:
            if height[l] > height[r]:
                i = r - 1
                while l < r and height[r] > height[i]:
                    i -= 1
                r = i
            else:
                i = l + 1
                while l < r and height[l] > height[i]:
                    i += 1
                l = i
            water = (r - l) * min(height[r], height[l])
            if best < water:
                best = water
        return best