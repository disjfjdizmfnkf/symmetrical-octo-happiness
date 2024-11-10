# 轮转数组 一个规律
class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
            l, r = 0, len(nums) - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r-1

            k %= len(nums)
            l, r = 0, k - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r-1

            l, r = k, len(nums) - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r-1
        


# 切片连接 
class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]
        # 如果是nums = nums[-k:] + nums[:-k] 则不是原地修改数组，这样原来的nums的对象被回收，指向现在新的对象


# 遍历 不推荐
class Solution0:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                if start == current:
                    break
            start += 1