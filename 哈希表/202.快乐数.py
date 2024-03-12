# 双指针   Floyd 循环检测 (运用快慢指针破循环)
class Solution:
    def isHappy(self, n: int) -> bool:
        """slow 指针每次走一步， fast 每次两步， 只要有环迟早都会相遇"""
        def sumOfDigits(n):
            res = 0
            while n:
                res += (n%10)*(n%10)
                n = n//10
            return res

        slow, fast = n, n
        while True:
            slow = sumOfDigits(slow)
            fast = sumOfDigits(fast)
            fast = sumOfDigits(fast)
            if fast == slow:
                break
        return slow == 1

# 常规做法
class Solution:
    def isHappy(self, n: int) -> bool:
        def happy_compute(num):
            if num < 10:
                return num * num
            bit = num%10
            return bit * bit + happy_compute(num // 10)
        visited = set()
        while n != 1:
            if n not in visited:
                visited.add(n)
                n = happy_compute(n)
            else:
                return False
        return True

