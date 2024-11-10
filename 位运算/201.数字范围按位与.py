class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        # 向右>>移位时相当于除以2 这里相与会使得m和n差距变小(m<n)直至相等
        while left < right:
            left >>= 1
            right >>= 1
            count += 1
        return left << count  # 还原位数