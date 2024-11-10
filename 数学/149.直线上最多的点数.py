

# 双层循环同 1.两数之和 的解法一， 表面上是要寻找所有符合条件的数，
#           ***但是里层循环都是从i+1开始的***
# 这种现象可以理解为在循环中通过限定内层循环的起始位置，避免处理已经处理过的元素，从而提高效率。
# 这种思想在很多题目中都有应用，比如 15.三数之和、18.四数之和、454.四数相加II 等等。
# 3.前提是这些元素都是相关的  ****是答案相互补充的部分****
# 2.这种现象出现的原因是因为在外层循环中已经处理过内层循环的起始位置之前的元素，所以不需要再次处理。
# 1.这种现象在一些题目中也  ****可以理解为去重**** ，比如 15.三数之和、18.四数之和 等等。
# 但是这种现象并不是所有题目都可以这么理解，比如 454.四数相加II，这道题目中的现象是因为两个数组是分开的，所以需要两层循环，而不是因为去重。

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        res = 0
        for i in range(len(points)):  # 寻找与点i在一条直线上的点
            duplicates = 1  # 与点i重合的点 一开始把自己算上 后边的遍历不会计算这个点
            hashMap = {'inf': 0}
            for j in range(i + 1, len(points)):  # 从i+1开始 i及之前的点在的直线之前的循环(外层)中已经遍历过了
                if points[i] == points[j]:
                    duplicates += 1  #
                elif points[i][0] == points[j][0]:
                    hashMap['inf'] += 1
                else:
                    k = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                    hashMap[k] = hashMap.get(k, 0) + 1
            res = max(res, max(hashMap.values()) + duplicates)
        return res