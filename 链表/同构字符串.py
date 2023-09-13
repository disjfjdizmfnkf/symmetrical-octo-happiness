#  t.length == s.length 
#  s 和 t 由任意有效的 ASCII 字符组成


#把第s和t的每一位字母映射到同一个数字上  hashMap
class Solution1:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMap1 = dict()
        hashMap2 = dict()
        n = len(s)
        for i in range(n):
            if hashMap1.get(s[i], 0) != hashMap2.get(t[i], 0): #如果同构，每个字符映射相同
                return False
            hashMap1[s[i]] = i + 1
            hashMap2[t[i]] = i + 1  #如果都没有映射（映射相同） 映射到新数字
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