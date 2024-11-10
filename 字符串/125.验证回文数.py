
# 运用python切片
class Solution1:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        for ss in s:
            if ss.isalpha():
                temp.append(ss.lower())
            elif ss.isdigit():
                temp.append(ss)
        return (res := ''.join(temp)) == res[::-1]


# 双指针  先处理字符串
"""
    c.isalnum() 判断一个字符是否为字母或数字,返回布尔值。
    c.lower() 将一个字符转换为小写。
    使用一个生成器表达式 (c.lower() for c in text if c.isalnum()) 从原始字符串中过滤出所有字母和数字字符,并将它们转换为小写。
    使用 ''.join(...) 将生成器表达式中的所有字符连接成一个新的字符串。
"""
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        cleanString = "".join(char.lower() for char in s if char.isalnum())
        l, r = 0, len(cleanString) - 1
        while l < r:
            if cleanString[l] != cleanString[r]:
                return False
            l += 1
            r -= 1
        return True
# 运用正则表达式

"""
sub函数：
    re.sub(pattern, repl, string, count=0, flags=0)
正则：
    [^a-zA-Z0-9]中的^表示否定，a-z、A-Z、0-9分别表示小写字母、大写字母和数字
"""
import re

class Solution3:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return s == s[::-1]