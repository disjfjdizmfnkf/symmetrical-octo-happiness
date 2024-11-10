
# 二分法
class Solution1:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        if x == 0:
            return 0

        left = 1
        right = x
        while left <= right:
            mid = (left + right) // 2
            if x < mid * mid:
                right = mid - 1
            if x > mid * mid:
                left = mid + 1
            if x == mid * mid:
                return mid
        return left - 1