"""给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。"""

# 递归
class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]: #把加一和进位的过程分开
        if digits[-1] < 9:
            digits[-1] += 1  #每次调用函数，最后一个数加一
            return digits
        elif len(digits) == 1 and digits[0] == 9: #首位为[9]
            return [1, 0]
        else:
            digits[-1] = 0  #每次调用函数，如果最后一个数=9，进位，让它=0，然后对前面的调用函数
            digits[0:-1] = self.plusOne(digits[0:-1])
            return digits


#遍历
class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        p = len(digits) - 1
        while digits[0] != 9 or p != 0:
            if digits[p] < 9:
                digits[p] += 1
                return digits
            else:
                digits[p] = 0
            p -= 1
        if digits[0] >= 9 and p == 0:
            digits[0] = 0
            return [1] + digits


#体会思想
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits 
        elif digits[0] == 9 and len(digits) == 1:
            return [1,0] #首位为9
        else:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits[:-1])
        return digits
             
            
