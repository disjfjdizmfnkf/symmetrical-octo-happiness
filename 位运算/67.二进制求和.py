
# 我他妈好累啊，代码还是要抽时间复习重新敲一次吧？
class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y        # 不考虑进位的加法，有效计算最后一位
            carry = (x & y) << 1  # 左移时自动补0
            x, y = answer, carry  # 此时carry后面为0 不影响x ^ y
        return bin(x)[2:]