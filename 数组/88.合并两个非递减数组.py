# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，
# 另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。
# 为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
# 示例 1：
# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
# 解释：需要合并 [1,2,3] 和 [2,5,6] 。
# 合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。


# 先合并再排序
class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()


#逆向双指针  由题意nums1后面为空，如果指针从后面遍历，把大的元素从后面开始放，就不用nums3变量
class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m+n-1
        while m > 0 and n > 0: #任意一个不为空（因为索引的关系）注意数组为空的条件是指针指0还是-1
            if  nums1[m-1] < nums2[n-1]:
                nums1[i] = nums2[n-1]
                n-=1
            else:
                nums1[i] = nums1[m-1]
                m-=1
            i-=1
        while n > 0 : #将数组2插入数组1，不确定那个先用完，这里如果数组2没完，接着换，如果不是就不用
            nums1[i] = nums2[n-1]
            n-=1
            i-=1

#一般双指针不能原地更改，不符合题意
class Solution3:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        sorted = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                sorted.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                sorted.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                sorted.append(nums1[p1])
                p1 += 1
            else:
                sorted.append(nums2[p2])
                p2 += 1
        nums1[:] = sorted
            
        