class Solution1:
    def trap(self, height: List[int]) -> int:
        """
            计算所有的积水只有两种情况:
            1. 左边界比右边界高的水坑
            2. 右边界比左边界高的水坑
        """
        total = 0
        left, right = 0, len(height) - 1
        l_most_hight, r_most_hight = 0, 0
        while left < right:
            if height[left] < height[right]:  # 最右侧高，计算左边堆积
                if l_most_hight < height[left]:
                    l_most_hight = height[left]
                else:  # 高度降低 && 最右侧比左侧高 -> 必定有积水
                    total += l_most_hight - height[left]
                # 移动边界重新判断，确保判断是否有水的方法是有效的
                left += 1
            else:  # 最左边>=右边，计算右边堆积
                if r_most_hight < height[right]:
                    r_most_hight = height[right]
                else:
                    total += r_most_hight - height[right]
                right -= 1
        return total


class Solution2:
    def water_count(self, left, right):
            if abs(left - right) == 1:
                return 0
            total = 0
            h = min(height[left], height[right])
            for i in range(left + 1, right):
                total += (h - height[i])
            return total
    
    def trap(self, height: List[int]) -> int:
        # 想法一： 两个方向各来一遍，左边界低于或等于与右边界的水池水 加上 右边界低于于左边界的水池水

        total = 0

        l, r = 0, 0
        while r < len(height):
            if height[r] >= height[l]:
                total += self.water_count(l, r)
                l = r
            r += 1

        height = height[::-1]

        l, r = 0, 0
        while r < len(height):
            if height[r] > height[l]:
                total += self.water_count(l, r)
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