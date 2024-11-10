#  t.length == s.length 
#  s 和 t 由任意有效的 ASCII 字符组成


# v1.0.0
#把第s和t的每一位字母映射到同一个数字上  hashMap
# class Solution1:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         """i + 1 为什么要加一? 一开始默认设定没有出现过的字符映射是0,而第一个i=0,
#         所以当之后出现的每一个新字符和i=0的字符判断都相等 [a,a]  [a,b] 会判断成相等"""
#         hashMap1 = dict()
#         hashMap2 = dict()
#         n = len(s)
#         for i in range(n):
#             if hashMap1.get(s[i], 0) != hashMap2.get(t[i], 0): #如果同构，每个字符映射相同
#                 return False
#             hashMap1[s[i]] = i + 1
#             hashMap2[t[i]] = i + 1  #如果都没有映射（映射相同） 映射到新数字
#         return True


#v2.0.0
class Solution1:
    # 同构就是将两个不同东西映射到一个相同的东西上
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        for i in range(len(s)):
            # false的情况:  两个字母映射的对象不同 或者 只有一个数字有映射(设置get默认值)
            if map1.get(s[i], -1) != map2.get(t[i], -1):
                return False
            else:
                map1[s[i]] = map2[t[i]] = i
        return True


#思路同上 但是是用数组完成映射
class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = [-1] * 256      #256 ASCII字符的个数
        map2 = [-1] * 256
        n = len(s)
        for i in range(n):
            if map1[ord(s[i])] != map2[ord(t[i])]:  #使用ord()将字符转化成ASCII编码，
                return False                    # 因为上个方案中字典哈希表的key可以是字符，所以没用
            map1[ord(s[i])] = i                 # 
            map2[ord(t[i])] = i
        return True