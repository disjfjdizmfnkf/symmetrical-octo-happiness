
#暴力求解
class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack) - len(needle) + 1):  # "hello"  "ll" 遍历四次
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

#KMP算法