class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p = m + n - 1
        p1 = m - 1
        p2 = n - 1
        while p2 >= 0:  # nums2没有合并完
            # 如果 p1 < 0，那么走 else 分支，把 nums2 合并到 nums1 中
            if nums1[p1] > nums2[p2] and p1 >= 0:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

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

        