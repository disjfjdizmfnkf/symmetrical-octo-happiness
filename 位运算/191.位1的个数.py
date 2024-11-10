
# 对于一个多位二进制数进行取模%2操作，实际上是在检查
# 这个数的最低位 (最右边的位) 是否为1，这是由二进制
# 数的性质决定的，和十进制取模%2是一样的这也是判断二
# 进制数奇偶性的一种方法


# & 逻辑与    Link：https://www.youtube.com/watch?v=5Km3utixwZs
class Solution1:
    """这样计算的效果类似于10000001 忽略了所有的0
    每次减一都改变了当前位置，其他位置都会被抵消掉相当于没有"""
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n = n&(n-1)
            res += 1
        return res

# 位移
class Solution2:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n%2
            n >> 1

        return res
