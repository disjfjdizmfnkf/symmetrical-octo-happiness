
# 双指针
class Solution:
    def maxArea(self, height: List[int]) -> int: # 越宽越高 越好
        # # 一开始最宽就好
        # l, r = 0, len(height) - 1
        # best = 0
        # most_height = max(height)
        # now_expected_best = most_height * (r - l)
        # while l < r:
        #     best = max(best, (r - l) * min(height[r], height[l]))
        #     if height[l] < height[r]: # 保证宽减小最少，但获得更高的边
        #         l += 1
        #     else:
        #         r -= 1
        # return best

        l, r = 0, len(height) - 1

        best = 0
        most_height = max(height)

        while l < r:
            best = max(best, (r - l) * min(height[r], height[l]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

            now_expected_best = most_height * (r - l)  # 方便理解now_expected_best 就是当前我们yy的最好结果
            if best >= now_expected_best:
                break

        return best