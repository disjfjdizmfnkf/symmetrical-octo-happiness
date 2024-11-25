# 使用递归
class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backTrack(combinations, remain):
            if not remain:
                res.append(combinations)
            # 同样是dfs 例如 1~4 k=2: 一般自己都是按 1,2 1,3 1,4 2,3 2,4 3,4 这种顺序
            for i in range(len(remain)):
                # 选择了第i个数之后，在不含这个数的数组中挑选其他的数
                backTrack(combinations + [remain[i]],
                          remain[:i] + remain[i+1:])
        backTrack([], nums)
        return res

# dfs


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(x):
            if x == len(nums)-1:
                ans.append(nums[:])
                return
            for i in range(x, len(nums)):
                nums[i], nums[x] = nums[x], nums[i]
                dfs(x+1)
                nums[i], nums[x] = nums[x], nums[i]
        ans = []
        dfs(0)
        return ans
