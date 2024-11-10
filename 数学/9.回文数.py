
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        rPart = 0  # 反转后的后半部分
        while x > rPart: # 结束时rPart >= x (取决于数字位数的奇偶)
            rPart = rPart*10 + x%10   #每次获得x最右边一位
            x = x//10                #去掉x最右边一位
        return rPart == x or rPart//10 == x