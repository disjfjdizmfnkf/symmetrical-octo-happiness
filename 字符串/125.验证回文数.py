
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
    char.isalnum() 数字和字符返回True 其他返回False
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