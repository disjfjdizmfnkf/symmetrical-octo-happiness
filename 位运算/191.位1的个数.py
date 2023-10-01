

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
            res += n%2 #模运算结果为最后一个数
            n >> 1

        return res