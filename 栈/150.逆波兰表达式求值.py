
# 乖乖用栈实现 python的基本语法
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        OPRN_stack = []
        for i in tokens:
            if i[-1].isdigit():  # python isdigit()判断不了负数
                OPRN_stack.append(int(i))
            else:
                b = OPRN_stack.pop()  # 默认弹出最外面的，队列使用pop(0) 弹出第一个(先进入的)
                a = OPRN_stack.pop()
                if i == '+':
                    OPRN_stack.append(int(a + b))
                if i == '-':
                    OPRN_stack.append(int(a - b))
                if i == '*':
                    OPRN_stack.append(int(a * b))
                if i == '/':
                    OPRN_stack.append(int(a / float(b)))  # python除法是向下取整
        return OPRN_stack.pop()

