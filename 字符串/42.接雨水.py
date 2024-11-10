class Solution:
    def trap(self, height: List[int]) -> int:
        # 想法一： 两个方向各来一遍，左边界低于或等于与右边界的水池水 加上 右边界低于于左边界的水池水
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
            if height[r] > height[l]:
                total += water_count(l, r)
                l = r
            r -= 1
        return total

        # 优化：遍历代替反转列表
        # l, r = len(height) - 1, len(height) - 1
        # while r < len(height) and l >= 0:
        #     if height[l] > height[r]:
        #         total += water_count(l, r)
        #         r = l
        #     l -= 1
        # return total

        # 优化：遍历代替反转列表和编列累计计算积水代替辅助函数
        # total = 0
        # left, right = 0, len(height) - 1
        # max_left, max_right = 0, 0

        # while left < right:
        #     if height[left] < height[right]:
        #         if height[left] > max_left:
        #             max_left = height[left]
        #         else:
        #             total += max_left - height[left]
        #         left += 1
        #     else:
        #         if height[right] > max_right:
        #             max_right = height[right]
        #         else:
        #             total += max_right - height[right]
        #         right -= 1
        # return total


        # 想法二： 从上往下一层一层削 ，未实现