class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 想到了滑动窗口，检查中间值和前后值的大小关系，但这个太难写了
        # 应该想到向前传递再向后传递来检查双方？ 为什么可以？
        n = len(ratings)
        res = [1]*n
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]: # 从左往右， 右边大于左边
                res[i] = res[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]: # 右边的是加过的判断给右边的加
                res[i] = max(res[i], res[i + 1] + 1) # 如果res中 左边大于右边就不需要加糖果了
        return sum(res)