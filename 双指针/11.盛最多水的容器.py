
#
class Solution:
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