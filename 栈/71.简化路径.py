class Solution:
    def simplifyPath(self, path: str) -> str:
        # 错误示例

        # stack = []
        # cur = ''
        # for char in path + '/':  # 为了有效划分最后一个
        #     if char == '/':  # 划分每个需要的操作
        #         if cur == '' or cur == '.':
        #             continue # 会跳过第15行代码，当前的cur不会被清空
        #         if cur == '..':
        #             if stack: stack.pop()
        #         else:
        #             stack.append(cur)
        #         cur = ''
        #     else:
        #         cur += char
        #
        # return '/' + '/'.join(stack)
        #
        # 输入
        # path =
        # "/a///b///c/d//././/.."
        # 输出
        # "/a/b"
        # 预期结果
        # "/a/b/c"

        stack = []
        cur = ''
        for char in path + '/':  # 为了有效划分最后一个
            if char == '/':  # 划分每个需要的操作
                if cur == '..':
                    if stack: stack.pop()
                elif cur != '' and cur != '.':
                    stack.append(cur)
                cur = ''
            else:
                cur += char

        return '/' + '/'.join(stack)