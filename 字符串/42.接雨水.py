class Solution:
    def trap(self, height: List[int]) -> int:
        def water_count(left, right):
            if abs(left - right) == 1:
                return 0
            total = 0
            h = min(height[left], height[right])
            for i in range(left + 1, right):
                total += (h - height[i])
            return total

        total = 0

        l, r = 0, 0
        while r < len(height):
            if height[r] >= height[l]:
                total += water_count(l, r)
                l = r
            r += 1

        height = height[::-1]
        l, r = 0, 0
        while r < len(height):
            if height[r] >= height[l]:
                total += water_count(l, r)
                l = r
            r += 1
        return total