

# 质因数分解  Link:
# 2 * 5 = 10
# 2的个数肯定比5多，所以只需要找出5的个数即可
# 5的个数 = n // 5 + n // 25 + n // 125 + ...
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        i = 5
        while n // i >= 1:
            count += n // i
            i *= 5
        return count