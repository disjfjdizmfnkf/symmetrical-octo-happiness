
# 分治和二分的思想


# 递归 时间复杂度O(log n)
class Solution1:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            n = -n
            x = 1 / x

        half = self.myPow(x, n // 2) #分治思想 求该问题的子问题 求它的一半
        if n % 2 == 0:
            return half * half
        else:
            return x * half * half

# 迭代
class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0.0

        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2

        return result
