class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 想到了滑动窗口，检查中间值和前后值的大小关系，但这个太难写了
        # 应该想到向前传递再向后传递来检查双方？ 为什么可以？
        n = len(ratings)
        res = [1]*n

        #  保证右边都比左边大(糖果数)，这也是为什么用右边和左边比较的原因
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                res[i] = res[i - 1] + 1  # 保证比右边大，不是简单的加1


        # 保证左边比右边大的糖果多    左边大的糖果多(满足条件的不变，保证糖果最少)
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]: # 右边的是加过的判断给右边的加
                res[i] = max(res[i], res[i + 1] + 1) # 如果res中 左边大于右边就不需要加糖果了
        return sum(res)