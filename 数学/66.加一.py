
# 递归  思考三种基本情况

"""三种基本情况：
             最后的数 < 9 直接加一 return
             最后的数也是第一个数 为 9


             递归情况 ： 第一个数之外的数为 9
"""
class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        if len(digits) == 1 and digits[-1] == 9:
            return [1,0]
        else:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits[:-1])   # 对需要的部分进行递归调用
            return digits