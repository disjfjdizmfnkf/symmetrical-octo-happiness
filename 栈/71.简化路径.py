class Solution:
    def simplifyPath(self, path: str) -> str:
        # 错误示例

        # stack = []
        # cur = ''
        # for char in path + '/':  # 为了有效划分最后一个
        #     if char == '/':  # 划分每个需要的操作
        #         if cur == '' or cur == '.':
        #             continue
        #         if cur == '..':
        #             if stack: stack.pop()
        #         else:
        #             stack.append(cur)
        #         cur = ''
        #     else:
        #         cur += char

        # return '/' + '/'.join(stack)

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