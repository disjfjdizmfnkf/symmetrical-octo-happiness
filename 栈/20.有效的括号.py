
# 用栈  字典(hashMap)辅助

class Solution1:
    def isValid(self, s: str) -> bool:
        dict = {'(':')','[':']','{':'}'}
        stack = []
        i = 0
        while i < len(s):
            if s[i] in dict:
                stack.append(s[i])
            else:
                if not stack or dict[stack.pop()] != s[i]:
                    return False
            i += 1
        return len(stack) == 0