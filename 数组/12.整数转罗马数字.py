
# 贪心算法
class Solution:
    def intToRoman(self, num: int) -> str:
        Map = [('M', 1000),
               ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
               ('XC', 90), ('L', 50), ('XL', 40), ('X', 10),
               ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]  # 可以组成所有数的基础罗马数字

        res = ""
        for n in Map:
            if n[1] <= num:
                res += n[0] * (num // n[1])
            num %= n[1]  # 取模， num减去最多个相同大小的数求剩下的等于他取这个数的模
        return res