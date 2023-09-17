"""最重要的思想是 一般大的字符在左边，小的在右边，
遇到特殊情况，小的在左边，大的在右边时，相当于减去左边的
也可以想，按照从左到右的顺序，相当于负的左边加右边"""

# 哈希表 按照从左到右的顺序相加 在一次遍历中只加一个变量
class Solution:
    # left < right:  -left + right 
    # left > right:   left + right
    def romanToInt(self, s: str) -> int:
        hashMap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = 0
        for i in range(len(s) - 1): #从第一个到倒数第二个
            if hashMap[s[i]] < hashMap[s[i+1]]:
                res -= hashMap[s[i]]
            else:
                res += hashMap[s[i]]
        return res + hashMap[s[-1]]    #加上最后一个
