

# 双指针
class Solution1:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0, 0
        while p1 < len(s) and p2 < len(t):
            if t[p2] == s[p1]:
                p1 += 1
            p2 += 1
        if p1 == len(s):
            return True
        else:
            return False
