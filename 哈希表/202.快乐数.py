






# 递归 + 哈希表    时间复杂度 O(不会算)
class Solution3:
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
