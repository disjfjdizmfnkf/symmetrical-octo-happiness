"""在寻找快乐数的时候会遇到循环 可能是1导致的 返回True 不是1导致的返回False"""

# 双指针   Floyd 循环检测 (运用快慢指针破循环)
class Solution:
    def isHappy(self, n: int) -> bool:
        """slow 指针每次走一步， fast 每次两步， 只要有环迟早都会相遇"""
        def sumOfDigits(n): # 除开递归的另一种算法
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


# 递归 + 哈希表    时间复杂度 O(不会算)
class Solution1_moreNeat:
    def isHappy(self, n: int) -> bool:
        def sumOfDigits(n):
            if n < 10:
                return n*n
            return (n%10)*(n%10) + sumOfDigits(n//10)
            
        hashSet = set()
        
        while n not in hashSet:
            hashSet.add(n)
            n = sumOfDigits(n)
            if n == 1:
                return True
        return False







class Solution1:
    def isHappy(self, n: int) -> bool:
        def happyNumber(n):
            if n < 10:
                return n*n
            else:
                return (n % 10)*(n % 10) + happyNumber(n//10)

        catch = {}
        while n > 0:
            if n not in catch:
                catch[n] = 1
            else:
                if n == 1:
                    return True
                return False
            n = happyNumber(n)
