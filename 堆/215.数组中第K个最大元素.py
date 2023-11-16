"""It's a pretty common case to have to work on data that is pre-sorted or near pre-sorted, so this
implementation with using the last element as the pivot isn't a good choice. Many people have suggested
picking a random element and switching it for the last element, but for arrays where every element has
 the same value that still leaves the input array sorted and still takes quadratic time. An additional
 improvement is to keep track of the last index < pivot and use that for the left window, instead of p-1
 . This eliminates processing duplicates of the pivot repeatedly. E.g.:"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k = n - k

        def quickselect(l, r):
            pivotIndex = random.randint(l, r)
            nums[pivotIndex], nums[r] = nums[r], nums[pivotIndex]

            pivot = nums[r]
            p = l
            lessEnd = -1
            for i in range(l, r):
                num = nums[i]
                if num < pivot:
                    lessEnd = p
                if num <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]

            if k > p:
                return quickselect(p + 1, r)
            elif k > lessEnd:
                return nums[p]
            else:
                return quickselect(l, lessEnd)

        return quickselect(0, n - 1)