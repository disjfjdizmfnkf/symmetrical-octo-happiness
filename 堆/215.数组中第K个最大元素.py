"""It's a pretty common case to have to work on data that is pre-sorted or near pre-sorted, so this
implementation with using the last element as the pivot isn't a good choice. Many people have suggested
picking a random element and switching it for the last element, but for arrays where every element has
 the same value that still leaves the input array sorted and still takes quadratic time. An additional
 improvement is to keep track of the last index < pivot and use that for the left window, instead of p-1
 . This eliminates processing duplicates of the pivot repeatedly. E.g.:"""


# [2, 31, 21,3, 4, 5 , 9, 11, 21]
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k   # 让第k大变成第len(nums)-k小，因为想让排序后的数组从小到大排列

        def quickselect(l, r):
            pivotIndex = random.randint(l, r)  # 随机找枢纽
            nums[pivotIndex], nums[r] = nums[r], nums[pivotIndex]

            pivot, p = nums[r], l
            lessEnd = -1
            for i in range(l, r):
                if nums[i] < pivot:
                    lessEnd = p   #  比枢纽小的数字个数，也是其下标
                if nums[i] <= pivot:       # 从左边开始，小于枢纽的和左边换，保证了小于枢纽的数字在左边
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]   # 把 p - 1 个比枢纽小的比较完后， 第p个位置换成枢纽

            if k > p:
                return quickselect(p + 1, r)
            elif k > lessEnd:
                return nums[p]
            else:
                return quickselect(l, lessEnd)

        return quickselect(0, len(nums) - 1)
