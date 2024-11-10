
# 用栈  字典(hashMap)辅助

class Solution1:
    def isValid(self, s: str) -> bool:
        dict = {'(':')','[':']','{':'}'}
        stack = []
        for c in s:
            if c in dict:
                # 左括号肯定先于右括号出现
                stack.append(c)
            else:
                if not stack or dict[stack.pop()] != c:
                    return False
        return len(stack) == 0