class Solution:
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
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        combine = []
        # 使用列表来模拟栈，pop()和append()操作
        # 递归的时候用列表作为combine，这样在递归调用的时候不会再创建新的字符串
        def backTrack(l_brackets, r_brackets):
            if r_brackets == n:
                res.append("".join(combine))
            if r_brackets < l_brackets:
                combine.append(')')
                backTrack(l_brackets, r_brackets + 1)
                combine.pop()
            if l_brackets < n:
                combine.append('(')
                backTrack(l_brackets + 1, r_brackets)
                combine.pop()

        backTrack(0, 0)
        return res
