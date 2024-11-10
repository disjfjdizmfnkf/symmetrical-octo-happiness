# 使用递归
class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backTrack(combinations, remain):
            if not remain:
                res.append(combinations)
            for i in range(len(remain)):
                backTrack(combinations + [remain[i]], remain[:i] + remain[i+1:])
        backTrack([], nums)
        return res

# dfs
class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(x):
            if x==len(nums)-1:
                ans.append(nums[:])
                return
            for i in range(x,len(nums)):
                nums[i],nums[x]=nums[x],nums[i]
                dfs(x+1)
                nums[i],nums[x]=nums[x],nums[i]
        ans=[]
        dfs(0)
        return ans