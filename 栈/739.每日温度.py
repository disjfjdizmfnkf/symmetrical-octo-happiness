# 单调栈
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # 用列表模拟栈
        for i in range(n):
            # 如果当前温度大于栈顶所指的温度，更新结果
            while stack and temperatures[i] > temperatures[stack[-1]]:
                top_ind = stack.pop()
                res[top_ind] = i - top_ind  # 正确计算等待天数
            stack.append(i)  # 将当前索引加入栈中
        return res