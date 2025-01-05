class Solution:
    # 方法一: 没有实现回溯，只是(实现了必要的递归)避免了无效的递归
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backTrack(combine, l_brackets, r_brackets):
            # base case
            if l_brackets == n and r_brackets == n:
                res.append(combine)
                return
            # 左括号数量小于 n 时都可以添加左括号
            if l_brackets < n:
                backTrack(combine + "(", l_brackets + 1, r_brackets)
            # 只能添加右括号，如果右括号数量小于左括号数量
            if r_brackets < l_brackets:
                backTrack(combine + ")", l_brackets, r_brackets + 1)

        backTrack("", 0, 0)
        return res

class Solution2:
    # 方法二: 回溯
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        combine = []
        def backTrack(l, r):
            if l == n and r == n:
                res.append(''.join(combine))  # 将数组连接成为字符串
            if l < n:
                combine.add("(")
                backTrack(l + 1, r)
                combine.pop()  # 恢复状态(递归结束回到这一层之后恢复之前的状态)
            if r < l:
                combine.add(")")
                backTrack(l, r + 1)
                combine.pop()
        backTrack(0, 0)
        return res
