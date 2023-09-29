
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